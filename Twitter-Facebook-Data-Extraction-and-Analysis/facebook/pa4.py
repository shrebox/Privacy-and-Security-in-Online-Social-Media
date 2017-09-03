import json
import matplotlib.pyplot as plt
from pymongo import MongoClient
import re
import facebook 
import requests
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

stock_words = ['it', 'is', 'an', 'a', 'the', 'of', 'out', 'this', 'that', 'has', 'to', 'you', '', 'in', 'for', 'they',
               '', 'i', 'them', 'no', 'are', 'am', 'w', 'who', 'will', 'there', 'all', 'if', 'on', 'and', 'we', 'with',
               'by', 'not', 'from', 'how', 'so', 'he', 'was', 'its', 'at', 'as', 'about', 'be', 'but', 'just', 'up']

def init():
    plotly.tools.set_credentials_file(username='shrebox', api_key='8Fho8pAor5uXorJsyukS')


#create a histogram for max occurring word in tweets
def create_word_histogram(word_dict, query):
    top_20 = {}

    count = 20
    for word in sorted(word_dict, key=word_dict.get, reverse=True):
        if word == 'fakenews' or word == '':
            continue
        top_20.update({word: word_dict[word]})
        count -= 1
        if count <= 0:
            break

    print(top_20)
    labels = []
    values = []
    for key in top_20.keys():
        print(key)
        labels.append(key)
        values.append(top_20.get(key))

    trace = go.Bar(x=labels, y=values)

    py.plot([trace], filename=query + '_bar_graph_twitter_most_common_words')

    print(query + " bar graph created : " + query + '_bar_graph_twitter_most_common_words')

def get_response_on_url(url):
    response = requests.get(url).json()
    return response

def get_timeline_posts_and_reactions(access_token):
    get_feed_url = 'https://graph.facebook.com/v2.10/me?access_token=' + access_token + '&debug=all&fields=id,name,feed{message,reactions}&format=json&method=get&pretty=0&suppress_http_code=1'
    response = requests.get(get_feed_url).json()
    return response

def get_reactions(post):
    all_reactions = []

    reactions = post['reactions']

    while True:
        all_reactions.extend(reactions['data'])

        if 'next' not in reactions['paging']:
            break
        else:
            next_reactions = get_response_on_url(reactions['paging']['next'])
            reactions = next_reactions

    return all_reactions


access_token = 'EAACEdEose0cBAAhSjXGKoiB4F1ZBTJ6FMmxvVH0xnDuWcluEZCsf0HMX52fiDPZCIXa59Wys9QWZCJdJCLVnlGMkXTBRMK3Y931xsBrqKDAM1QzLrcCWfzx2IUeLLOvWyRBHVZC2gtfVIugoRZB6pFRySbxV6ETNvzEj7tyCf6bVAcrK1MvyY3sLWIagTiRUXPntpupYMekAZDZD'

user_feed = get_timeline_posts_and_reactions(access_token)

all_messages = []
all_reactions = []

# todo put this into a while loop which takes pagination into account.
# todo figure out what is taking so long for this piece of $H!T to execute.

# print(user_feed)

client = MongoClient()
db = client['facebook_db']
collection_posts = db['posts']
collection_reactions = db['reactions']

for post in user_feed['feed']['data']:
    if 'message' in post:
        all_messages.append(post['message'])
    if 'reactions' in post:
        all_reactions.extend(get_reactions(post))

print('added all messages')

reaction_counts = {}

for reaction in all_reactions:
    if 'name' in reaction:
        name = reaction['name']
        if name in reaction_counts:
            reaction_counts[name] += 1
        else:
            reaction_counts.update({name: 1})

print('count of reactions' + str(len(all_reactions)))

all_words = []

for message in all_messages:
    for word in message.split():
        word = re.sub('[^A-Za-z0-9]+', '', word.lower())
        all_words.append(word)

word_count = {}
for word in all_words:
    if word not in stock_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count.update({word: 1})

init()

create_word_histogram(word_count, 'fb_posts')

create_word_histogram(reaction_counts, 'fb_reactions')





