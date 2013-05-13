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
        hashtags_text_list[index] = hashtags['text']
        index = index + 1
        break

for key, value in hashtags_text_list.iteritems():
    print value