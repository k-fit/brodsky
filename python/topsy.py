import urllib
import sys
sys.path.append("..")
import keys
import otter # easy_install python-otter

print keys.topsy_apikey

# otter library doesn't seem to need my api key
# but if you do use it, you get more calls (I think)
# put apikey=xxxxxx in ~/.otterrc

kw = otter.loadrc()

#query = "Whitney Houston"

query = raw_input("Enter query: ")


# STEP 1, set the resource
# STEP 2, make the call with the right parameters
# STEP 3, read the results.  r.response.o is the full JSON response
# but r.response.list.o is the list of actual results
# r.next_page() takes you to the next page of results


# find expert contributors to a query
r = otter.Resource('experts', **kw)
r(q = query)

for item in r.response.list.o:
    print item['name'], item['influence_level']


# search for content related to the query over the last hours, days, etc
r = otter.Resource('search', **kw)
r(q = query, window = 'd')

for item in r.response.list.o:
    print item['firstpost_date'], item['mytype'], item['trackback_total'], item['score']

# get top 100 for the day, can also set 1k, 5k.  Can set different types or take all types.
r = otter.Resource('top', **kw)
r(thresh = 'top100', type = 'tweet')

for k in range(3):
    for item in r.response.list.o:
        print item['author_name'], item['content'], item['date_alpha']
    r.next_page()


# search histogram - counts unique links related to query
# default is one bin per day for the past 30 days
r = otter.Resource('searchhistogram', **kw)
r(q = query)

print r.response.o['histogram']


# search count.  dynamic = 1 means it looks for what it thinks is the best window.
r = otter.Resource('searchcount', **kw)
r(q=query, dynamic = 1)

print r.response.o


# list of trending terms - different than "top"
r = otter.Resource('trending', **kw)
r()

print r.response.list.o
