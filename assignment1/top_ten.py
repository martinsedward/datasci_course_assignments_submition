import json
import urllib
import sys
import re


tweets = []
tweet_file = open(sys.argv[1])

for line in tweet_file:#Line
#try: 
    tweets.append(json.loads(line))
#except:

ids = []
hashtags_text_list = {}
index = 0

for tweet in tweets:
    if tweet['entities']['hashtags']:
        for hashtags in tweet['entities']['hashtags']:
            hashtags_text_list[index] = hashtags['text'].lower()
            index = index + 1
            break

hashtags_text = {}
for key, value in hashtags_text_list.iteritems():
    score = 0.0
    for key_aux, value_aux in hashtags_text_list.iteritems():
        if value == value_aux:
            score = score + 1
    hashtags_text[value] = score

count = 0
for key, value in sorted(hashtags_text.iteritems(), key=lambda (k,v): (v,k), reverse=True): 
    if count < 10:
        print key, value
        count = count + 1
    else:
        break