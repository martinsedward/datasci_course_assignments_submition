#import simplejson
import json
import urllib
#import urllib2
import sys
import re

#Open sentiment file score and transform in dict 
afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

  
#Open fw the sentiment file to output
sentiment_file = open(sys.argv[1],'w')

#Open fr the livestream data
tweet_file = open(sys.argv[2])

#will use to split from the space between the words
pattern_split = re.compile(r"\W+")

score = 0
for jsonstring in tweet_file:#Line
    for word in pattern_split.split(json.loads(jsonstring)["text"].lower()):#Words of line
    #    sentiment_file.write("[" + word +" = " + str(scores.get(word, 0)) + "]")
    #sentiment_file.write("\n")    
        score = score + scores.get(word, 0)
    sentiment_file.write(str(score) + "\n") 
    score = 0
        

#json = simplejson.load(urllib.urlopen("http://search.twitter.com/search.json?q=pfizer"))
#json = simplejson.load(tweet_file)

#print scores



#sentiment_file.write("teste1" + "\n")
#sentiment_file.write("teste2" + "\n")


tweet_file.close()
sentiment_file.close()

  
#print scores.items() # Print every (term, score) pair in the dictionary

