# -*- coding: utf-8 -*-
import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
#print json.load(response)
lresponse = json.load(response)
#print type(lresponse)
#print lresponse.keys()
#print lresponse['page']
#print lresponse['results_per_page']
#print type(lresponse['results'])
#print lresponse['results']
results = lresponse['results']
#print type(results[0])
#print results[0].keys()
#print str(results[0]['from_user_id_str'])
for number in range(10):
    print results[number]['from_user_id_str']
    print results[number]['text']

