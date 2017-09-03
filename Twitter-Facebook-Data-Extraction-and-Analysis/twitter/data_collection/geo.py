import json
# Tweets are stored in in file "fname". In the file used for this script, 
# each tweet was stored on one line
fname = 'fakenewsq.json'
with open(fname, 'r') as f:
    with open('fn4.json', 'w') as fout:
    
        #Create dictionary to later be stored as JSON. All data will be included
        # in the list 'data'
        users_with_geodata = {
            "data": []
        }
        all_users = []
        total_tweets = 0
        geo_tweets  = 0
        for line in f:
            tweet = json.loads(line)
            if tweet['user']['id']:
                total_tweets += 1 
                user_id = tweet['user']['id']
                if user_id not in all_users:
                    all_users.append(user_id)
                    
                    #Give users some data to find them by. User_id listed separately 
                    # to make iterating this data later easier
                    user_data = {
                        "user_id" : tweet['user']['id'],
                        "features" : {
                            "name" : tweet['user']['name'],
                            "id": tweet['user']['id'],
                            "screen_name": tweet['user']['screen_name'],
                            "tweets" : 1,
                            "location": tweet['user']['location'],
                        }
                    }
                    #Iterate through different types of geodata to get the variable primary_geo
                    '''if tweet['coordinates']:
                        user_data["features"]["primary_geo"] = str(tweet['coordinates'][tweet['coordinates'].keys()[1]][1]) + ", " + str(tweet['coordinates'][tweet['coordinates'].keys()[1]][0])
                        user_data["features"]["geo_type"] = "Tweet coordinates"'''
                    if tweet['place']:
                        user_data["features"]["primary_geo"] = tweet['place']['country']
                        user_data["features"]["geo_type"] = "Tweet place"
                    else:
                        user_data["features"]["primary_geo"] = None
                        user_data["features"]["geo_type"] = None
                    '''elif tweet['place']:
                        user_data["features"]["primary_geo"] = tweet['place']['full_name'] + ", " + tweet['place']['country']
                        user_data["features"]["geo_type"] = "Tweet place"
                    else:
                        user_data["features"]["primary_geo"] = tweet['user']['location']
                        user_data["features"]["geo_type"] = "User location"'''
                    
                    #Add only tweets with some geo data to .json. Comment this if you want to include all tweets.
                    if user_data["features"]["primary_geo"]:
                        users_with_geodata['data'].append(user_data)
                        fout.write(json.dumps(user_data) + '\n')
                        geo_tweets += 1
                
                #If user already listed, increase their tweet count
                elif user_id in all_users:
                    for user in users_with_geodata["data"]:
                        if user_id == user["user_id"]:
                            user["features"]["tweets"] += 1
        
        #Count the total amount of tweets for those users that had geodata            
        for user in users_with_geodata["data"]:
            geo_tweets = geo_tweets + user["features"]["tweets"]
        #Get some aggregated numbers on the data
        print "The file included " + str(len(all_users)) + " unique users who tweeted with or without geo data"
        print "The file included " + str(len(users_with_geodata['data'])) + " unique users who tweeted with geo data, including 'location'"
        print "The users with geo data tweeted " + str(geo_tweets) + " out of the total " + str(total_tweets) + " of tweets."
    # Save data to JSON file
    '''with open('pp4.json', 'w') as fout:
        fout.write(json.dumps(users_with_geodata) + '\n')'''