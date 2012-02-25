import urllib
import sys
sys.path.append("..")
import keys
import oauth2 as oauth

# easy_instal gdata
import gdata.youtube 
import gdata.youtube.service

'''
yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True
yt_service.developer_key = keys.youtube_developer_key

yt_service.email = "test"
yt_service.password = "test"

yt_service.ProgrammaticLogin()
'''

client = gdata.youtube.service.YouTubeService()

'''
the client knows about all kinds of shit.  I don't see us using more than these (and not all of these I hope)
apparently we don't need a key to access this stuff.  I haven't quite figured out the authentication business - but I can see these feeds
client.GetMostDiscussedVideoFeed           
client.GetMostLinkedVideoFeed             
client.GetMostRecentVideoFeed              
client.GetMostRespondedVideoFeed           
client.GetMostViewedVideoFeed 
client.GetRecentlyFeaturedVideoFeed       
client.GetTopFavoritesVideoFeed            
client.GetTopRatedVideoFeed                
client.GetUserFavoritesFeed               
client.GetWatchOnMobileVideoFeed           
client.GetWithRetrie
client.GetYouTubeRelatedVideoFeed
'''

feed = client.GetRecentlyFeaturedVideoFeed()
for entry in feed.entry:
    print entry.title.text, entry.rating.average

feed = client.GetMostViewedVideoFeed()
for entry in feed.entry:
    print entry.title.text, entry.rating.average

feed = client.client.GetMostLinkedVideoFeed()
for entry in feed.entry:
    print entry.title.text

# there's all kinds of stuff you can access about each video.  some potentially interesting ones:
'''
entry.statistics.view_count
entry.statistics.favorite_count
entry.statistics.subscriber_count
entry.statistics.video_watch_count
entry.rating.max min num_raters
entry.category - a long fucking list of categories
entry.updated.text
'''
