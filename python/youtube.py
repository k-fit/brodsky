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

feed = client.GetRecentlyFeaturedVideoFeed()
for entry in feed.entry:
    print entry.title.text, entry.rating.average

feed = client.GetMostViewedVideoFeed()
for entry in feed.entry:
    print entry.title.text, entry.rating.average

feed = client.client.GetMostLinkedVideoFeed()
for entry in feed.entry:
    print entry.title.text

# there's all kinds of stuff you can access about the video.  some potentially interesting ones:
'''
entry.statistics.view_count
entry.statistics.favorite_count
entry.statistics.subscriber_count
entry.statistics.video_watch_count
entry.rating.max min num_raters
entry.category - a long fucking list of categories
entry.updated.text
'''
