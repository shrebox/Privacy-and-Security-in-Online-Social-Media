from apiclient.discovery import build
import argparse
import csv
import unidecode

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCzrdvj9rQKBSmpIWHk5-Zwyd9ZtM04VIw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(q=options.q, part="id,snippet", maxResults=options.max_results).execute()
    
    videos = []
    channels = []
    playlists = []

    # create a CSV output for video list    
    csvFile = open('video_result.csv','w')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["title","description","videoId","viewCount","likeCount","dislikeCount","commentCount","channelTitle","CviewCount","CcommentCount","subscriberCount"])
    channelID = ""
    nextPageToken = ""
    
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    while search_response.get("items",[]) is not None:
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                title = search_result["snippet"]["title"]
                title = unidecode.unidecode(title)  
                description = search_result["snippet"]["description"]
                description = unidecode.unidecode(description)
                channelID = search_result["snippet"]["channelId"]
                videoId = search_result["id"]["videoId"]
                video_response = youtube.videos().list(id=videoId,part="statistics").execute()
                for video_result in video_response.get("items",[]):
                    viewCount = video_result["statistics"]["viewCount"]
                    if 'likeCount' not in video_result["statistics"]:
                        likeCount = 0
                    else:
                        likeCount = video_result["statistics"]["likeCount"]
                    if 'dislikeCount' not in video_result["statistics"]:
                        dislikeCount = 0
                    else:
                        dislikeCount = video_result["statistics"]["dislikeCount"]
                    if 'commentCount' not in video_result["statistics"]:
                        commentCount = 0
                    else:
                        commentCount = video_result["statistics"]["commentCount"]
                    
                #getting channel content
                channel_reponse = youtube.channels().list(id=channelID,part="snippet,statistics").execute()
                for channel_result in channel_reponse.get("items",[]):
                    channelTitle = channel_result["snippet"]["title"]
                    channelTitle = unidecode.unidecode(channelTitle)
                    viewCCount = channel_result["statistics"]["viewCount"]
                    if 'commentCount' not in channel_result["statistics"]:
                        commentCCount = 0
                    else:
                        commentCCount = channel_result["statistics"]["commentCount"]
                    if 'subscriberCount' not in channel_result["statistics"]:
                        subscriberCount = 0
                    else:
                        subscriberCount = channel_result["statistics"]["subscriberCount"]
                        
                csvWriter.writerow([title,description,videoId,viewCount,likeCount,dislikeCount,commentCount,channelTitle,viewCCount,commentCCount,subscriberCount])
    
            #getting the next page token
            nextPageToken = search_response["nextPageToken"]
          
        #updating the search response with the next page token attribute      
        search_response = youtube.search().list(q=options.q, part="id,snippet", maxResults=options.max_results, pageToken=nextPageToken).execute()

    csvFile.close()
    
      
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search on YouTube')
    parser.add_argument("--q", help="Search term", default="Google")
    parser.add_argument("--max-results", help="Max results", default=50)
    args = parser.parse_args()
    youtube_search(args)
