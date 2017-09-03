import json
import matplotlib.pyplot as plt

with open('pp4.json','r') as f:

	dict = {}

	for line in f:

		tweet = json.loads(line)

		#print tweet['features']['primary_geo']

		if tweet['features']['primary_geo'] not in dict:
			dict[tweet['features']['primary_geo']] = 0
		dict[tweet['features']['primary_geo']] += 1

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

with open('fn4.json','r') as f:

	dict = {}

	for line in f:

		tweet = json.loads(line)

		#print tweet['features']['primary_geo']

		if tweet['features']['primary_geo'] not in dict:
			dict[tweet['features']['primary_geo']] = 0
		dict[tweet['features']['primary_geo']] += 1

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