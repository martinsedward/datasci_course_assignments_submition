#import simplejson
import json
import urllib
#import urllib2
import sys
import re

try:
    #Open sentiment file score and transform in dict 
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
      
    #Open fr the livestream data
    tweet_file = open(sys.argv[2])
    
    #will use to split from the space between the words
    pattern_split = re.compile(r"\W+")
    
    score = 0
    scored_tweet = {}#lines containing tweet sentiment scored based in words of AFINN-111
    scored_tweet_list = {}
    zero_word_list = {}#lines containing words does not contained in AFINN-111
    scored_tweet_aux = ""
    index = 0
    
    #open tweet stream file, score the words and summarize the tweet, create zero word list 
    for jsonstring in tweet_file:#Line
        for word in pattern_split.split(json.loads(jsonstring)["text"].lower()):#Words of line
            #receive the score.
            score_aux = scores.get(word, 0)
            #increment sum of socore    
            score = score + score_aux
            #increment scored tweet line contain words and tweet sentiment
            scored_tweet_aux = scored_tweet_aux + " " +  word + " "#the words are separet for spaces
            #if word isnt contained in AFINN-111 the score is 0
            if score_aux == 0:
                #populate a zero-word list
                if len(word) > 2:#populate a zero-word list without space, and 2 letters word like "is", "or", etc
                    zero_word_list[word] = word
        #print str(score)
        #increment the sumatized score value ot tweet
        scored_tweet_list[index] = str(score) + "\t" + scored_tweet_aux#the tweet are separate for tab
        #after use, clear all
        scored_tweet_aux = ""
        score = 0
        index = index + 1
        
    #check
    for key, value in scored_tweet_list.iteritems() :
        print key, value
    #print zero_word_list
    
    #Close all opened files
    tweet_file.close()
    afinnfile.close()
    
    #based on the summarized tweet list, count positive and negative zero words apears
    #read zero word list
    score_aux = 0
    for key, word in zero_word_list.iteritems():
    #word = 'friend'
        for key, value in scored_tweet_list.iteritems():
            score, list_term  = value.split("\t")
            if re.search(r"\s" + str(word) + "\s",  list_term):
                if int(score) > 0:
                    #print str(word) + " - FOUND & POSITIVE"
                    score_aux = score_aux + 1
                elif  int(score) < 0:
                    #print str(word) + " - NOT FOUND & NEGATIVE"
                    score_aux = score_aux - 1
            #else:
            #    score_aux = score_aux + 0
                #print str(word) + " - NOT FOUND"
        print str(word), str(score_aux)
        score_aux = 0
except: 
    pass