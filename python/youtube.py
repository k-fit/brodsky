import urllib
import sys
sys.path.append("..")
import keys
import oauth2 as oauth

# easy_instal gdata
import gdata.youtube 
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True
yt_service.developer_key = keys.youtube_developer_key

yt_service.email = "test"
yt_service.password = "test"

yt_service.ProgrammaticLogin()
