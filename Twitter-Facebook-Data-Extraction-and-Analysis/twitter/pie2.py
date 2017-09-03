import json
import matplotlib.pyplot as plt

with open('panamapapersq2.json','r') as f:

	dict = {}

	for line in f:

		tweet = json.loads(line)

		#print type(tweet['entities']['hashtags'])

		if tweet['entities']['hashtags']:
			if 'hashtags' not in dict:
				dict['hashtags'] = 0
			dict['hashtags'] += 1

		if tweet['entities']['symbols']:
			if 'symbols' not in dict:
				dict['symbols'] = 0
			dict['symbols'] += 1

		if tweet['entities']['urls']:
			if 'urls' not in dict:
				dict['urls'] = 0
			dict['urls'] += 1

		if tweet['entities']['user_mentions']:
			if 'user_mentions' not in dict:
				dict['user_mentions'] = 0
			dict['user_mentions'] += 1

		if tweet['entities'].get('media'):
			if 'media' not in dict:
				dict['media'] = 0
			dict['media'] += 1


print dict

labels = []
values = []

for val in dict:
	values.append(dict[val])
	labels.append(val)

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(values, labels=labels, colors=colors,
	autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

with open('fakenewsq.json','r') as f:

	dict = {}

	for line in f:

		tweet = json.loads(line)

		#print type(tweet['entities']['hashtags'])

		if tweet['entities']['hashtags']:
			if 'hashtags' not in dict:
				dict['hashtags'] = 0
			dict['hashtags'] += 1

		if tweet['entities']['symbols']:
			if 'symbols' not in dict:
				dict['symbols'] = 0
			dict['symbols'] += 1

		if tweet['entities']['urls']:
			if 'urls' not in dict:
				dict['urls'] = 0
			dict['urls'] += 1

		if tweet['entities']['user_mentions']:
			if 'user_mentions' not in dict:
				dict['user_mentions'] = 0
			dict['user_mentions'] += 1

		if tweet['entities'].get('media'):
			if 'media' not in dict:
				dict['media'] = 0
			dict['media'] += 1


print dict

labels = []
values = []

for val in dict:
	values.append(dict[val])
	labels.append(val)

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(values, labels=labels, colors=colors,
	autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()


