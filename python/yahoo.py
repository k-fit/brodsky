import urllib
import sys
sys.path.append("..")
import keys

#url = 'http://www.cnn.com/2011/11/11/world/europe/greece-main/index.html'

def getYahooContent(u):
    key = keys.ydn_key #querylang = "http://query.yahooapis.com/v1/public/yql?q=select * from contentanalysis.analyze where url=\'"+u +"\';&diagnostics=true&format=json&" + key
    
    try:
	jresult = eval(urllib.urlopen(querylang).read())
	categories = jresult['query']['results']['yctCategories']['yctCategory']
    	entities = jresult['query']['results']['entities']['entity']
        
    	elist = []
    	for e in entities:
            elist.append( {'score' : e['score'], 'text' : e['text']['content'] } )
        return ({'categories' : categories, 'entities' : elist})
    except:
	return({'categories' : [], 'entities' : []})

    

