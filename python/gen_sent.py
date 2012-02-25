import urllib
import sys
sys.path.append("..")
import keys
import oauth2 as oauth

def print_content(title, content):
    print title
    print content


c_key = keys.gen_sent_key
c_secret = keys.gen_sent_secret

consumer = oauth.Consumer(key=c_key,secret=c_secret)
client = oauth.Client(consumer)


# SENTIMENT
url = "http://qa.generalsentiment.com:8080/api/v1.php/getSentiment"
params = {"entityName": "Barack Obama", "startDate": "20110801", "endDate" : "20110901", "timeUnit" : "day", "src" : "all_internet" , "include_reference_polarity_count" : "true" }
r_method= "POST"

r_body = urllib.urlencode(params,doseq=True).replace('+','%20')
response,content = client.request(url,method=r_method,body=r_body)

print_content("sentiment", content)

# INVOLVEMENT
url2 = "http://qa.generalsentiment.com:8080/api/v1.php/getInvolvement"
params = {"synsets": "Google\tgoogle\tGOOG\nMicrosoft\tMSFT\nObama\tBarack Obama", "startDate": "20110801", "endDate" : "20110901" }

r_method= "POST"
r_body = urllib.urlencode(params,doseq=True).replace('+','%20')
response,content = client.request(url,method=r_method,body=r_body)

print_content("involvement", content)

# MEDIA VALUE per DAY
url = "http://qa.generalsentiment.com:8080/api/v1.php/getMVR"
params = {"synset": "Google\tgoogle\tGOOG", "startDate": "20110801", "endDate" : "20110901", "mvType" : "impact" }

r_method= "POST"
r_body = urllib.urlencode(params,doseq=True).replace('+','%20')
response,content = client.request(url,method=r_method,body=r_body)

print_content("media value per day", content)


# JUXTAPOSITION?
url = "http://qa.generalsentiment.com:8080/api/v1.php/getJuxta"
params = {"synset": "Google\tgoogle\tGOOG", "startDate": "20110801", "endDate" : "20110901", "top_count" : "25", "src" : "all_internet" }

r_method= "POST"
r_body = urllib.urlencode(params,doseq=True).replace('+','%20')
response,content = client.request(url,method=r_method,body=r_body)

print_content("juxtaposition", content)


# SENTIMENT + VOLUME ("momentum"?)
url = "http://qa.generalsentiment.com:8080/api/v1.php/getSentimentAndVolumeForSynset"
params = {"synset": "Obama\tBarack Obama\tPresident Obama", "startDate": "20110801", "endDate" : "20110901", "timeUnit" : "day", "src" : "all_internet" , "include_reference_polarity_count" : "true" , "smooth_sentiment" : "false" }

r_method= "POST"
r_body = urllib.urlencode(params,doseq=True).replace('+','%20')
response,content = client.request(url,method=r_method,body=r_body)

print_content("sentiment and volume", content)


# SEARCH NEWS ARTICLES
url = "http://qa.generalsentiment.com:8080/api/v1.php/searchArticlesForSynset"
params = {"synset": "Google\tgoogle\tGOOG", "startDate": "20110801", "endDate" : "20110901", "src": "news", "articles_limit": "20" }

r_method= "POST"
r_body = urllib.urlencode(params,doseq=True).replace('+','%20')
response,content = client.request(url,method=r_method,body=r_body)

print_content("search news articles", content)
