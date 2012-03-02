import urllib
import sys
sys.path.append("..")
import keys
import otter
from gen_sent_fun import *
from yahoo import *

kw = otter.loadrc()

def topsy(time_unit = 'day', src = 'all_internet', call = 'top100'):
        r = otter.Resource('top', **kw)
        r(thresh = call, locale = 'en', perpage = 100) # note if call > 100, better do something else
        if (call != 'top100'):
            print "you didn't change this yet"
            sys.exit(1)
        important_data = []
        while (len(r.response.list.o)) :
            important_data += r.response.list.o
            r.next_page()
        #print "done"
        
        for i in range(len(important_data)):  
        # call topsy histogram api, record histogram
                h = otter.Resource('searchhistogram', **kw)
                h(q = important_data[i]['target']['title'], slice = 3600, period = 24 * 30)
                important_data[i]['histogram'] = h.response.o['histogram']
                
                important_data[i]['yahoo'] = getYahooContent(important_data[i]['target']['url'])
                important_data[i]['gen_sent'] = []
                for k in range(len(important_data[i]['yahoo']['entities'])) : 
                        important_data[i]['gen_sent'].append (gen_sent(important_data[i]['yahoo']['entities'][k]['text'], start_date='20120215', end_date = '20120301', src = src, time_unit = time_unit))
        print important_data[i]

