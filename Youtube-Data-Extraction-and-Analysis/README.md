# PreCog-Task

  <h2>1. Data extraction using the search_keyword.py script:</h2>
  Using the Youtube API v3, data has been extracted for a particular keyword by giving command-line parameters. I have  collected data for ~500 videos for a particular keyword (in my case "ted"). 

The data extracted includes video's "title","description","videoId","viewCount","likeCount","dislikeCount","commentCount" and channel's "channelTitle","viewCount","commentCount","subscriberCount". 
As youtube allows only 25 results/page, I have used pagination using the "nextPageToken" to get the next page results.
  
  To use the script, in terminal run the following command:
 <b> $ python search_keyword.py --q keyword_to_search</b>

  <h2>2. Webapp for the data analysis:</h2>
  Data collected in part 1 has been analysed using the Google Charts.
  To check the webapp, open it on a browser or host it on local server using the following command in the directory where the     analysis.html is located:
  <b>$ python -m SimpleHTTPServer.</b>
  This would host the webapp on the local server on the address "localhost:8000". Page is also hosted on:  https://youtube-analysis-precogtask.herokuapp.com/
  <h2>3. Predicting the number of likes on a YouTube video URL one can input:</h2>
  This task has to be done for the collected data.
  

  
  
