import sys, os, tweepy, time
from tweepy import OAuthHandler
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from os import path

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

d = path.dirname(__file__)



mask = np.array(Image.open(path.join(d, "trump_mask.png")))




while(True):
  time.sleep(21600) # Change to frequency you want
  text = open("words.txt").read()
  wc = WordCloud(max_words=250, mask=mask, margin=10,
               random_state=1, width=2048, height=2048).generate(text)
  wc.to_file("trumpCloud.png")
  with open('words.txt', 'w') as fi:
    fi.write('')
    api.update_with_media('trumpCloud.png', '')
    print 'Tweet published'	
