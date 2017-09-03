import facebook
import json
import requests	
import matplotlib.pyplot as plt

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAI95ccXQHKSzlXsHX9idZCaNusJV8lpEkxQMOZAVxFnC4tccuqTkNUZBC6rs80EywzDgEsQPnqjtQhwrfU4qCaxMulcSjisBF4VgbNZB5KvMJAf3kprHSsV7QWicyY7WPnMQtsqsKnRPcb3ZCuSfqyuTgPIffVoV96yguFxRloWjHRqciMZAKdZAi2fQgDnGwZDZD')

loc = graph.get_connections (id='me',connection_name='friends?fields=birthday')

dict = {}

while(True):
	for val in loc['data']:
		if 'birthday' in val:
			a = val['birthday'].split('/')
			if a[0] not in dict:
				dict[a[0]] = 0
			dict[a[0]] += 1

	flag = 0
	if 'paging' in loc:
		if 'next' in loc['paging']:
			loc = requests.get(loc['paging']['next']).json()
		else:
			flag = 1
	if flag == 1:
		break

print dict

x= [1,2,3,4,5,6,7,8,9,10,11,12]
y = [dict['01'],dict['02'],dict['03'],dict['04'],dict['05'],dict['06'],dict['07'],dict['08'],dict['09'],dict['10'],dict['11'],dict['12']]
label = ["January","Februrary","March","April","May","June","July","August","September", "October","November","December"]

plt.xticks(x, label)
plt.plot(x,y)
plt.show()



