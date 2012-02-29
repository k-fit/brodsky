import urllib
import sys
sys.path.append("..")
import keys
import oauth2 as oauth



def gen_sent(input_words, start_date, end_date, src, time_unit):
	c_key = keys.gen_sent_key
	c_secret = keys.gen_sent_secret

	consumer = oauth.Consumer(key=c_key,secret=c_secret)
	client = oauth.Client(consumer)
	
	if time_unit != "day" and time_unit != "month" and time_unit != "year" and time_unit != "total":
		print "Warning: time_unit must be either one of day, month, year or total"
		sys.exit()

	if src != "all_internet" and src != "news" and src != "twitter" and src != "social" and src != "websites":
		print "Warning: src must be either all_internet, news, twitter, social, or websites"
		sys.exit()


	url = "http://qa.generalsentiment.com:8080/api/v1.php/getSentiment"
	
	params = {"entityName": str(input_words), "startDate": str(start_date), "endDate" : str(end_date), "timeUnit" : str(time_unit), "src" : str(src), "include_reference_polarity_count" : "true" }
	
	r_method= "POST"
	
	r_body = urllib.urlencode(params,doseq=True).replace('+','%20')
	
	response,content = client.request(url,method=r_method,body=r_body)

	l = len(eval(content)['results'])
	#print l 	
	#print eval(content)
	return {'dates': [eval(content)['results'][i]['date'] for i in range(l)], 'pos_ref': [eval(content)['results'][i]['positive_references'] for i in range(l)], 'neg_ref': [eval(content)['results'][i]['negative_references'] for i in range(l)], 'ref': [eval(content)['results'][i]['references'] for i in range(l)], 'sentiment': [eval(content)['results'][i]['sentiment'] for i in range(l)] }

	
	
