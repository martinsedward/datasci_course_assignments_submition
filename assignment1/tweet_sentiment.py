import simplejson
#import json
#import urllib
import urllib2
import sys

#Open dictio score sentiment file
afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.
  
#Open fw the sentiment file to output
sentiment_file = open(sys.argv[1],'w')

#Open fr the livestream data
tweet_file = open(sys.argv[2])

for jsonstring in tweet_file:
        print simplejson.loads(jsonstring)["text"]



#json = simplejson.load(urllib.urlopen("http://search.twitter.com/search.json?q=pfizer"))
#json = simplejson.load(tweet_file)

#print json


#sentiment_file.write("teste1" + "\n")
#sentiment_file.write("teste2" + "\n")


tweet_file.close()
sentiment_file.close()

  
#print scores.items() # Print every (term, score) pair in the dictionary

