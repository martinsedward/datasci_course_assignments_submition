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
#    pass

#tweet = tweets[0]
#print tweet

ids = []
for tweet in tweets:
  if tweet['entities']['hashtags']:
    print tweet['entities']['hashtags'][0]['text']
    break