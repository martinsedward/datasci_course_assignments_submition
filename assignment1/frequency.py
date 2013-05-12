import json
import urllib
import sys
import re

try:
    #Open fr the livestream data
    tweet_file = open(sys.argv[1])
    
    #will use to split from the space between the words
    pattern_split = re.compile(r"\W+")
    
    #load all words contained in tweet to a dict
    dict_word = {}
    tweet = {}
    tweet_aux = ""
    index = 0
    for jsonstring in tweet_file:#Line
        for word in pattern_split.split(json.loads(jsonstring)["text"].lower()):#Words of line
            if len(word) > 2:
                dict_word[word] = word
                tweet_aux = tweet_aux  + " " + word + " "        
        tweet[index] = tweet_aux
        index = index +1
        tweet_aux = ""
    #close all opened files
    tweet_file.close()
    
    #count the words to determine the frenquency
    word_count = 0
    word_count_list = {}
    for key, word in dict_word.iteritems():
        for key, tweet_list in tweet.iteritems():
            if re.search(r"\s" + str(word) + "\s",  tweet_list):
                word_count = word_count + 1
        word_count_list[word] = word_count
        word_count = 0
    
    
    #check
    #for key, value in tweet.iteritems():
    #    print value
    #for key, value in dict_word.iteritems():
    #    print value    
    for key, value in word_count_list.iteritems():
        print key, value    
except: 
    pass