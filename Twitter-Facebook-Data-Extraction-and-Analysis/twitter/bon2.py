import tweepy
import sys
import os


#Pass our consumer key and consumer secret to Tweepy's user authentication handler
auth = tweepy.AppAuthHandler("bQG4SoprwuNR8uOZxY2KimwEb", "FpFFb9Vs1cWIgRnU76FekZJqxf8O2baNHHnLPqVNXneOVFRT64")

api = tweepy.API(auth,wait_on_rate_limit=True,
                   wait_on_rate_limit_notify=True)
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

fname = sys.argv[1]

user = api.get_user(fname)

statuses = []

for status in tweepy.Cursor(api.user_timeline, id=fname).items():
        statuses.append(status)

flag = 0
val = ""

for status in reversed(statuses):
    if flag == 0:
        val = status.text
    flag = 1

print val


