#import simplejson
import json
import urllib
#import urllib2
import sys
import re

try:
    #Open sentiment file score and transform in dict 
    #afinnfile = open("AFINN-111.txt")
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
    #Open fw the sentiment file to output
    #sentiment_file = open('sentiment_file_derived.txt','w')
    
    #Open fr the livestream data
    tweet_file = open(sys.argv[2])
    
    #will use to split from the space between the words
    pattern_split = re.compile(r"\W+")
    
    score = 0
    word_aux = ""
    state_aux = ""
    #index = 0
    
    UF = {}
    for jsonstring in tweet_file:#Line
        if json.loads(jsonstring)['place'] != None:
            if str(json.loads(jsonstring)['place']['country_code']) == 'US':
                #for key, value in state.iteritems():
                #    if str(json.loads(jsonstring)['place']['name']) in key:#check if the citie in place.name are a valid citie of US state
                for word in pattern_split.split(json.loads(jsonstring)["text"].lower()):#Words of line
                    score = score + scores.get(word, 0)
                    word_aux = word_aux + str(word) + " "
                    citie, value = json.loads(jsonstring)['place']['full_name'].split(",")
                    state_aux = json.loads(jsonstring)['place']['country_code'] + " - " + citie + " - " + value #  + " - " + json.loads(jsonstring)['user']['location']
                
                print str(score),state_aux, " - [" + word_aux + "]"
                #Calculate whats the more happy state
                for key_uf, value_uf in UF.iteritems():
                    score_uf, uf  = value_uf.split("\t")
                    if str(uf) == str(value):
                        score = score + int(score_uf)
                    
                UF[value] = str(score) + "\t" +value
                #index = index + 1
                
                score = 0
                state_aux = ""
                word_aux = ""
                break
          
    
    tweet_file.close()
    afinnfile.close()
    #Calculate whats the more happy state
    Happy_UF = ""
    score_aux = -100
    for key, value in sorted(UF.iteritems(), key=lambda (k,v): (v,k)):
        score, uf  = value.split("\t")
        if int(score) > score_aux:
            score_aux = int(score)
            Happy_UF = uf
        print "%s: %s" % (score, uf)
        
    print "Happiest UF is "+Happy_UF + " with " + str(score_aux)
    #print Happy_UF
except: 
    pass    
