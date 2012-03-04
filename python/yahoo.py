import urllib
import sys
sys.path.append("..")
import keys
import BeautifulSoup
import re
from unidecode import unidecode
import ast


#url = 'http://www.cnn.com/2011/11/11/world/europe/greece-main/index.html'

def getYahooContent(u):
    key = keys.ydn_key
    querylang = "http://query.yahooapis.com/v1/public/yql?q=select * from contentanalysis.analyze where url=\'"+u +"\';&diagnostics=true&format=json&" + key
    
    jresult = queryattempt(querylang)
    if not jresult:
	print "getting text"
	text = getURLContent(u)
	querylang =  "http://query.yahooapis.com/v1/public/yql?q=select * from contentanalysis.analyze where text=\'"+ text +"\';&diagnostics=true&format=json&" + key
	jresult = queryattempt(querylang)
    if not jresult:      
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


def getURLContent(u, thresh = 50):
    html = urllib.urlopen(u).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    texts = soup.findAll(text=True)
    visible_texts = filter(visible, texts)
    alltext = ""
    for line in visible_texts:
        if len(line) > thresh:
	    line = unidecode(line)
	    line = line.replace("]", "")
	    line = line.replace("[", "")
	    line = line.replace("'", "")
	    line = line.replace("&", "\&")
            alltext += line.strip() + " "
    return alltext;

def queryattempt(query):
    try:
	jresult = ast.literal_eval(urllib.urlopen(query).read())
	return jresult
    except:
	return None

	
