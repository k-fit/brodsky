import urllib
import sys
sys.path.append("..")
import keys
import BeautifulSoup
import re
from unidecode import unidecode
import ast
import time



def getAlchemy(url):
        categories = getAlchemyCat(url)
 	keywords = getAlchemyKey(url)
	concepts = getAlchemyCon(url)
	return ({'categories' : categories, 'keywords' : keywords, 'concepts': concepts})


def getAlchemyCat(url):
	key = keys.alch_key
	queryCat = "http://access.alchemyapi.com/calls/url/URLGetCategory?apikey="+key+"&url=" + url + "&outputMode=json"
	result_cat = queryattempt(queryCat)
	return result_cat

def getAlchemyKey(url):
	key = keys.alch_key
	queryKey = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey="+key+"&url=" + url + "&outputMode=json"	
	result_key = queryattempt(queryKey)
	return result_key


def getAlchemyCon(url):
	key = keys.alch_key
	queryKey = "http://access.alchemyapi.com/calls/url/URLGetRankedConcepts?apikey="+key+"&url=" + url + "&outputMode=json"	
	result_con = queryattempt(queryCon)
	return result_con


def queryattempt(query):
    attempt = 0 
    jresult = None
    while not jresult and attempt < 2:
	try:
	    attempt += 1
	    r = urllib.urlopen(query).read()
	    r = r.replace('\r', '')
	    r = r.replace('\n', '')
	    jresult = ast.literal_eval(r)
	    return jresult
	except:
	    #print "waiting three second****************"
	    time.sleep(1)
	    jresult = None
    return jresult
