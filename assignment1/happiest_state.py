#import simplejson
import json
import urllib
#import urllib2
import sys
import re

#Open sentiment file score and transform in dict 
#afinnfile = open("AFINN-111.txt")
afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

#US Cities and States
state = {}
state['Birmingham']='AL'
state['Montgomery']='AL'
state['Mobile']='AL'
state['Huntsville']='AL'
state['Anchorage']='AK'
state['Phoenix']='AZ'
state['Tucson']='AZ'
state['Mesa']='AZ'
state['Chandler']='AZ'
state['Glendale']='AZ'
state['Scottsdale']='AZ'
state['Gilbert']='AZ'
state['Tempe']='AZ'
state['Peoria']='AZ'
state['Surprise']='AZ'
state['Little Rock']='AR'
state['Los Angeles']='CA'
state['San Diego']='CA'
state['San Jose']='CA'
state['San Francisco']='CA'
state['Fresno']='CA'
state['Sacramento']='CA'
state['Long Beach']='CA'
state['Oakland']='CA'
state['Bakersfield']='CA'
state['Anaheim']='CA'
state['Santa Ana']='CA'
state['Riverside']='CA'
state['Stockton']='CA'
state['Chula Vista']='CA'
state['Fremont']='CA'
state['Irvine']='CA'
state['San Bernardino']='CA'
state['Modesto']='CA'
state['Oxnard']='CA'
state['Fontana']='CA'
state['Moreno Valley']='CA'
state['Glendale']='CA'
state['Huntington Beach']='CA'
state['Santa Clarita']='CA'
state['Garden Grove']='CA'
state['Oceanside']='CA'
state['Santa Rosa']='CA'
state['Rancho Cucamonga']='CA'
state['Ontario']='CA'
state['Lancaster']='CA'
state['Corona']='CA'
state['Elk Grove']='CA'
state['Palmdale']='CA'
state['Salinas']='CA'
state['Pomona']='CA'
state['Torrance']='CA'
state['Hayward']='CA'
state['Escondido']='CA'
state['Sunnyvale']='CA'
state['Orange']='CA'
state['Pasadena']='CA'
state['Fullerton']='CA'
state['Thousand Oaks']='CA'
state['Visalia']='CA'
state['Simi Valley']='CA'
state['Concord']='CA'
state['Roseville']='CA'
state['Santa Clara']='CA'
state['Victorville']='CA'
state['Vallejo']='CA'
state['El Monte']='CA'
state['Berkeley']='CA'
state['Downey']='CA'
state['Costa Mesa']='CA'
state['Inglewood']='CA'
state['San Buenaventura (Ventura)']='CA'
state['Carlsbad']='CA'
state['West Covina']='CA'
state['Norwalk']='CA'
state['Fairfield']='CA'
state['Murrieta']='CA'
state['Richmond']='CA'
state['Burbank']='CA'
state['Antioch']='CA'
state['Temecula']='CA'
state['Daly City']='CA'
state['El Cajon']='CA'
state['Rialto']='CA'
state['Santa Maria']='CA'
state['Denver']='CO'
state['Colorado Springs']='CO'
state['Aurora']='CO'
state['Fort Collins']='CO'
state['Lakewood']='CO'
state['Thornton']='CO'
state['Westminster']='CO'
state['Pueblo']='CO'
state['Arvada']='CO'
state['Centennial']='CO'
state['Bridgeport']='CT'
state['New Haven']='CT'
state['Hartford']='CT'
state['Stamford']='CT'
state['Waterbury']='CT'
state['Washington']='DC'
state['Jacksonville']='FL'
state['Miami']='FL'
state['Tampa']='FL'
state['St. Petersburg']='FL'
state['Orlando']='FL'
state['Hialeah']='FL'
state['Tallahassee']='FL'
state['Fort Lauderdale']='FL'
state['Port St. Lucie']='FL'
state['Pembroke Pines']='FL'
state['Cape Coral']='FL'
state['Hollywood']='FL'
state['Gainesville']='FL'
state['Miramar']='FL'
state['Coral Springs']='FL'
state['Miami Gardens']='FL'
state['Clearwater']='FL'
state['Palm Bay']='FL'
state['Pompano Beach']='FL'
state['West Palm Beach']='FL'
state['Atlanta']='GA'
state['Augusta']='GA'
state['Columbus']='GA'
state['Savannah']='GA'
state['Athens']='GA'
state['Honolulu']='HI'
state['Boise']='ID'
state['Chicago']='IL'
state['Aurora']='IL'
state['Rockford']='IL'
state['Joliet']='IL'
state['Naperville']='IL'
state['Springfield']='IL'
state['Peoria']='IL'
state['Elgin']='IL'
state['Indianapolis']='IN'
state['Fort Wayne']='IN'
state['Evansville']='IN'
state['South Bend']='IN'
state['Des Moines']='IA'
state['Cedar Rapids']='IA'
state['Davenport']='IA'
state['Wichita']='KS'
state['Overland Park']='KS'
state['Kansas City']='KS'
state['Topeka']='KS'
state['Olathe']='KS'
state['Louisville']='KY'
state['Lexington']='KY'
state['New Orleans']='LA'
state['Baton Rouge']='LA'
state['Shreveport']='LA'
state['Lafayette']='LA'
state['Baltimore']='MD'
state['Boston']='MA'
state['Worcester']='MA'
state['Springfield']='MA'
state['Lowell']='MA'
state['Cambridge']='MA'
state['Detroit']='MI'
state['Grand Rapids']='MI'
state['Warren']='MI'
state['Sterling Heights']='MI'
state['Ann Arbor']='MI'
state['Lansing']='MI'
state['Flint']='MI'
state['Minneapolis']='MN'
state['Saint Paul']='MN'
state['Rochester']='MN'
state['Jackson']='MS'
state['Kansas City']='MO'
state['St. Louis']='MO'
state['Springfield']='MO'
state['Independence']='MO'
state['Columbia']='MO'
state['Billings']='MT'
state['Omaha']='NE'
state['Lincoln']='NE'
state['Las Vegas']='NV'
state['Henderson']='NV'
state['Reno']='NV'
state['North Las Vegas']='NV'
state['Manchester']='NH'
state['Newark']='NJ'
state['Jersey City']='NJ'
state['Paterson']='NJ'
state['Elizabeth']='NJ'
state['Albuquerque']='NM'
state['New York']='NY'
state['Buffalo']='NY'
state['Rochester']='NY'
state['Yonkers']='NY'
state['Syracuse']='NY'
state['Charlotte']='NC'
state['Raleigh']='NC'
state['Greensboro']='NC'
state['Durham']='NC'
state['Winston Salem']='NC'
state['Fayetteville']='NC'
state['Cary']='NC'
state['Wilmington']='NC'
state['High Point']='NC'
state['Fargo']='ND'
state['Columbus']='OH'
state['Cleveland']='OH'
state['Cincinnati']='OH'
state['Toledo']='OH'
state['Akron']='OH'
state['Dayton']='OH'
state['Oklahoma City']='OK'
state['Tulsa']='OK'
state['Norman']='OK'
state['Broken Arrow']='OK'
state['Portland']='OR'
state['Eugene']='OR'
state['Salem']='OR'
state['Gresham']='OR'
state['Philadelphia']='PA'
state['Pittsburgh']='PA'
state['Allentown']='PA'
state['Erie']='PA'
state['Providence']='RI'
state['Columbia']='SC'
state['Charleston']='SC'
state['Sioux Falls']='SD'
state['Memphis']='TN'
state['Nashville']='TN'
state['Knoxville']='TN'
state['Chattanooga']='TN'
state['Clarksville']='TN'
state['Murfreesboro']='TN'
state['Houston']='TX'
state['San Antonio']='TX'
state['Dallas']='TX'
state['Austin']='TX'
state['Fort Worth']='TX'
state['El Paso']='TX'
state['Arlington']='TX'
state['Corpus Christi']='TX'
state['Plano']='TX'
state['Laredo']='TX'
state['Lubbock']='TX'
state['Garland']='TX'
state['Irving']='TX'
state['Amarillo']='TX'
state['Grand Prairie']='TX'
state['Brownsville']='TX'
state['Pasadena']='TX'
state['Mesquite']='TX'
state['McKinney']='TX'
state['McAllen']='TX'
state['Killeen']='TX'
state['Waco']='TX'
state['Carrollton']='TX'
state['Frisco']='TX'
state['Beaumont']='TX'
state['Abilene']='TX'
state['Denton']='TX'
state['Midland']='TX'
state['Round Rock']='TX'
state['Wichita Falls']='TX'
state['Odessa']='TX'
state['Richardson']='TX'
state['Salt Lake City']='UT'
state['West Valley City']='UT'
state['Provo']='UT'
state['West Jordan']='UT'
state['Virginia Beach']='VA'
state['Norfolk']='VA'
state['Chesapeake']='VA'
state['Richmond']='VA'
state['Newport News']='VA'
state['Alexandria']='VA'
state['Hampton']='VA'
state['Seattle']='WA'
state['Spokane']='WA'
state['Tacoma']='WA'
state['Vancouver']='WA'
state['Bellevue']='WA'
state['Kent']='WA'
state['Everett']='WA'
state['Milwaukee']='WI'
state['Madison']='WI'
state['Green Bay']='WI'



  
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
            for key, value in state.iteritems():
                if str(json.loads(jsonstring)['place']['name']) in key:#check if the citie in place.name are a valid citie of US state
                    for word in pattern_split.split(json.loads(jsonstring)["text"].lower()):#Words of line
                        score = score + scores.get(word, 0)
                        word_aux = word_aux + str(word) + " "
                        state_aux = json.loads(jsonstring)['place']['country_code'] + " - " + json.loads(jsonstring)['place']['name'] + " - " + value #  + " - " + json.loads(jsonstring)['user']['location']
                    
                    #print str(score),state_aux, " - [" + word_aux + "]"
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
    #print "%s: %s" % (score, uf)
    
#print "Happiest UF is "+Happy_UF + " with " + str(score_aux)
print Happy_UF

