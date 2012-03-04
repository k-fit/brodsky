import urllib
import sys
sys.path.append("..")
import otter
import re
from unidecode import unidecode
import ast
import pprint
import time
import keys
from gen_sent_fun import *
from yahoo import *
from hist_plot import *

kw = otter.loadrc()

def topsy(time_unit = 'day', src = 'all_internet', call = 'top100', p = 0, debug = 0):
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
	print "done"
        
        for i in range(len(important_data)):  
        # call topsy histogram api, record histogram
            h = otter.Resource('searchhistogram', **kw)
	    #print important_data[i]
	    title = unidecode(important_data[i]['target']['title'])
	    url = unidecode(important_data[i]['target']['url'])
            print title, url
	    h(q = title, slice = 3600, period = 24 * 30)
            important_data[i]['histogram'] = h.response.o['histogram']
            attempt = 0
	    important_data[i]['yahoo'] = getYahooContent(url, debug)
            while important_data[i]['yahoo']['categories'] == [] and attempt < 3:
		time.sleep(1)
		attempt += 1
		important_data[i]['yahoo'] = getYahooContent(url, debug)
	    important_data[i]['gen_sent'] = []

            for k in range(len(important_data[i]['yahoo']['entities'])) : 
                important_data[i]['gen_sent'].append (gen_sent(important_data[i]['yahoo']['entities'][k]['text'], start_date='20120215', end_date = '20120301', src = src, time_unit = time_unit))

	    print "result: " 
	    pprint.pprint(important_data[i])
<<<<<<< HEAD
	
#	hist_plot(important_data)
	return important_data
=======
	if p:
	    hist_plot(important_data)
	#return important_data
>>>>>>> 29bbeef22a5b1024efe002d17f2a27eb612c0229

if __name__ == '__main__':
    topsy(debug = 1)
