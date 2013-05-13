import json
import urllib
import sys
import re

#Open fr the livestream data
tweet_file = open(sys.argv[1])

hashtags_text_list = {}
index = 0

for jsonstring in tweet_file:#Line
    try:
        if str(json.loads(jsonstring)['place']['country_code']) == 'US':
            hashtags_text_list[hashtags] = json.loads(jsonstring)['user']['entities']['hashtags']['text']
            
    except:
        pass

for value in hashtags_text_list.iteritems():
    print value

tweet_file.close()
