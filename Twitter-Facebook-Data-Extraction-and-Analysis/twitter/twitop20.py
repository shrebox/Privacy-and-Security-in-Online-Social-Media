import re
import operator 
import json
from collections import Counter
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
import numpy as np
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions	
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

punctuation = list(string.punctuation)
stop = set(stopwords.words('english') + punctuation + ['rt', 'via','RT','#FakeNews','#PanamaPapers','17','6','12.08','10.75','The','You','would','This','I','said','Now','ever'])
xaxis1 = []
yaxis1 = []
xaxis2 = []
yaxis2 = []
test1 = []
test2 = []

fname = 'fakenewsq.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # Update the counter
        count_all.update(terms_stop)
    # Print the first 5 most frequent words
    print(count_all.most_common(21))
    for count in range(1,21):
    	xaxis1.append(count_all.most_common(21)[count][0])
    	yaxis1.append(count_all.most_common(21)[count][1])

fname = 'panamapapersq.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # Update the counter
        count_all.update(terms_stop)
    # Print the first 5 most frequent words
    print(count_all.most_common(21))
    for count in range(1,21):
    	xaxis2.append(count_all.most_common(21)[count][0])
    	yaxis2.append(count_all.most_common(21)[count][1])
    #print len(xaxis1)

numb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

plt.bar(numb, yaxis1, align='center')
plt.xticks(numb, xaxis1)
plt.show()

plt.bar(numb, yaxis2, align='center')
plt.xticks(numb, xaxis2)
plt.show()