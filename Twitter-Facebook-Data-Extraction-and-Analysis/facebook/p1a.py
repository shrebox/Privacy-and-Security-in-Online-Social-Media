import facebook
import json
import requests	
import matplotlib.pyplot as plt

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAI95ccXQHKSzlXsHX9idZCaNusJV8lpEkxQMOZAVxFnC4tccuqTkNUZBC6rs80EywzDgEsQPnqjtQhwrfU4qCaxMulcSjisBF4VgbNZB5KvMJAf3kprHSsV7QWicyY7WPnMQtsqsKnRPcb3ZCuSfqyuTgPIffVoV96yguFxRloWjHRqciMZAKdZAi2fQgDnGwZDZD')

loc = graph.get_connections (id='me',connection_name='friends?fields=location')

dict = {}

while(True):
	for val in loc['data']:
		if 'location' in val:
			if val['location']['name'] not in dict:
				dict[val['location']['name']] = 0
			dict[val['location']['name']] += 1

	flag = 0

	if 'paging' in loc:
		if 'next' in loc['paging']:
			loc = requests.get(loc['paging']['next']).json()
		else:
			flag = 1
	if flag == 1:
		break

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





