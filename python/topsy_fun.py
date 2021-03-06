import urllib
import sys
sys.path.append("..")
import otter
import re
from unidecode import unidecode
import ast
import pprint
import keys
from gen_sent_fun import *
from yahoo import *
from alchemy import *
from hist_plot import *
import datetime

kw = otter.loadrc()

def topsy(startday, stopday, time_unit = 'day', src = 'all_internet', call = 'top100', p = 1, debug = 0):
        r = otter.Resource('top', **kw)
        r(thresh = call, locale = 'en', perpage = 10) # note if call > 100, better do something else
        if (call != 'top100'):
            print "you didn't change this yet"
            sys.exit(1)
        important_data = []
        #important_data += r.response.list.o # for testing, just take the first 10
	while (len(r.response.list.o)) :
            important_data += r.response.list.o
            r.next_page()
	    print len(important_data)
	    if debug:
		if len(important_data) >= 100: break
	print "done"
        
        for i in range(len(important_data)):  
        # call topsy histogram api, record histogram
            h = otter.Resource('searchhistogram', **kw)
	    print important_data[i]
	    title = unidecode(important_data[i]['target']['title'])
	    url = unidecode(important_data[i]['target']['url'])
            print title, url
	    try:
		    h(q = title, slice = 3600, period = 24 * 30)
	    except:
		    continue
	    try:
		    important_data[i]['histogram'] = h.response.o['histogram']
	    except:
		important_data[i]['histogram'] = []
            attempt = 0
	    important_data[i]['yahoo'] = getYahooContent(url, debug)
	    #important_data[i]['alchemy'] = getAlchemy(url)
	    important_data[i]['gen_sent:yahoo'] = []
	    #important_data[i]['gen_sent:alchemy'] = []


            for k in range(len(important_data[i]['yahoo']['entities'])) : 
                important_data[i]['gen_sent:yahoo'].append(gen_sent(important_data[i]['yahoo']['entities'][k]['text'], start_date=startday, end_date = stopday, src = src, time_unit = time_unit))
            #for k in range(len(important_data[i]['alchemy']['keywords'])) :      
	     #    import_data[i]['gen_sent:alchemy'].append(gen_sent(important_data[i]['alchemy']['keywords'][k]['text'], start_date=startday, end_date = stopday, src = src, time_unit = time_unit))

	    print "result: " 
	    pprint.pprint(important_data[i])
	    pprint.pprint(important_data[i]['yahoo'])
	    #pprint.pprint(important_data[i]['alchemy'])
  	    #raw_input("press to continue bitches!: ")
	    
#
	
#	hist_plot(important_data)
#	return important_data

	if p:
	    hist_plot(important_data[0:100])

if __name__ == '__main__':
    today = datetime.datetime.now()
    twoweeksago = today - datetime.timedelta(days = 14)
    today = today.strftime("%Y%m%d")
    twoweeksago = twoweeksago.strftime("%Y%m%d") 
    topsy(debug = 1, startday = twoweeksago, stopday = today)
