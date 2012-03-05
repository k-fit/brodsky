import urllib
import sys
sys.path.append("..")
import keys
import BeautifulSoup
import re
from unidecode import unidecode
import ast
import time

#url = 'http://www.cnn.com/2011/11/11/world/europe/greece-main/index.html'

def getYahooContent(u, debug):
    key = keys.ydn_key
    querylang = "http://query.yahooapis.com/v1/public/yql?q=select * from contentanalysis.analyze where url=\'"+u +"\';&diagnostics=true&format=json&" + key
    
    jresult = queryattempt(querylang)
    
    if not jresult:
	print "getting text"
	text = getURLContent(u, debug)
	querylang =  "http://query.yahooapis.com/v1/public/yql?q=select * from contentanalysis.analyze where text=\'"+ text +"\';&diagnostics=true&format=json&" + key
	jresult = queryattempt(querylang)
    
    if not jresult:     
	if debug:
	    print querylang 
	return({'categories' : [], 'entities' : []})
    
    try:
	categories = jresult['query']['results']['yctCategories']['yctCategory']
    except:
	categories = []
    
    try:    
	entities = jresult['query']['results']['entities']['entity']
    except:
	entities = []
    
    elist = []
    tags = set()
    if type(entities) == type(dict()):
	entities = [entities]
    
    for e in entities:
	if e['text']['content'] not in tags:
	    elist.append( {'score' : e['score'], 'text' : e['text']['content'] } )
	    tags.add(e['text']['content'])
    return ({'categories' : categories, 'entities' : elist})
        
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:  # don't read text from these types of fields
        return False
    elif re.match('<!--.*-->', str(element)): # don't read texts out of comments
        return False
    return True


def getURLContent(u, debug = 0, thresh = 50):
    html = urllib.urlopen(u).read()
    try:
	soup = BeautifulSoup.BeautifulSoup(html)
    except:
	return ""
    texts = soup.findAll(text=True)
    visible_texts = filter(visible, texts)
    alltext = ""
    for line in visible_texts:
	if debug:
	    if len(line) > 25: print line
        if len(line) > thresh:
	    line = unidecode(line)
	    line = line.replace("]", "")
	    line = line.replace("[", "")
	    line = line.replace("'", "")
	    line = line.replace("&", "")
	    line = line.replace("#", "")
            alltext += line.strip() + " "
    return alltext;

def queryattempt(query):
    attempt = 0 
    jresult = None
    while not jresult and attempt < 3:
	try:
	    attempt += 1
	    jresult = ast.literal_eval(urllib.urlopen(query).read())
	    return jresult
	except:
	    print "waiting three second****************"
	    time.sleep(d)
	    jresult = None
    return jresult

	
