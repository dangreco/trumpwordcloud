import json, sys, os, tweepy, string, excludeDict
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key = ''
consumer_secret = ''

access_token = ''
access_secret = ''

# TWITTER API BUILDING
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
printable = set(string.printable)



class MyListener(StreamListener):


    def on_data(self, data):
      d = json.loads(data)
      if 'text' in d:
        txt = d['text']
        txt = filter(lambda x: x in printable, txt)
        with open('words.txt', 'a') as fi:
          for word in txt.lower().split():
            if not excludeDict.excludeWord(str(word)):
              fi.write(word  + '\n')
          fi.close()

    def on_error(self, status):
        print(status)
        return True

# --------------------------------------

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Trump', "Donald", "Donald Trump"])
