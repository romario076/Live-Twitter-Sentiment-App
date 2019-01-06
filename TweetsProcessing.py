import os
import numpy as np
import pandas as pd
from tweepy import Stream, API
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sqlite3
import json
from unidecode import unidecode
from textblob import TextBlob
import re
from threading import Thread, Lock, Event
import time
from datetime import datetime
from Config import RunConfig
from tweetsSideCounter import TweetsSideCounter
import time


class listener(StreamListener):
    def __init__(self, TweetsProcessing, dbName, tableName):
        self.TweetsProcessing = TweetsProcessing
        self.tableName = tableName
        self.conn = sqlite3.connect(dbName,  check_same_thread=False)
        self.c = self.conn.cursor()


    def on_data(self, data):
        tweet = ""
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            tweet = tweet.replace("\'", "").replace("'", "''").replace('"', "''").replace("&", "&&").strip()
            tweet = re.sub(r'\s*https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
            if len(tweet)>0:
                time_ms = data['timestamp_ms']
                polarity = TextBlob(tweet).sentiment.polarity
                self.TweetsProcessing.tweetsCounter.update(polarity=polarity)
                print(str(datetime.fromtimestamp(float(time_ms)/1000)), polarity)
                self.c.execute("""INSERT INTO """ + self.tableName + """ (UnixTime, Tweet, Polarity) VALUES (%s, "%s", %f)"""
                               % (time_ms, tweet, polarity))
                self.conn.commit()
                time.sleep(0.2)
                #time.sleep(0.1)
        except Exception as e:
            print(str(type(e)) + ": " + str(e))
            print(tweet)
        return(True)

    def on_error(self, status):
        print (status)


class TweetsProcessing(Thread):
    def __init__(self, ckey, csecret, atoken, asecret, dbName, tableName, keyWords=[]):
        #Thread.__init__(self, group=None, target=None, name='TweetsProcessing')
        self.ckey = ckey
        self.csecret = csecret
        self.atoken = atoken
        self.asecret = asecret
        self.dbName = dbName
        self.tableName = tableName
        self.keyWords = keyWords
        self.tweetsCounter = TweetsSideCounter()

        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """

        thread = Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()

    # def checkKeyWordsUpdates(self):
    #     while True:
    #         reload(Config)
    #         from Config import RunConfig
    #         self.keyWords = RunConfig.keyWords
    #         print ("KeyWords: " + str(self.keyWords))
    #         time.sleep(2)

    def createTwitterDB(self):
        try:
            conn = sqlite3.connect(self.dbName)
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS %s(UnixTime REAL, Tweet VARCHAR(300), Polarity REAL)" % (self.tableName))
            conn.commit()
            c.execute("CREATE INDEX fast_unix ON %s(UnixTime)" % (self.tableName))
            c.execute("CREATE INDEX fast_tweet ON %s(Tweet)" % (self.tableName))
            c.execute("CREATE INDEX fast_sentiment ON %s(Polarity)" % (self.tableName))
            c.execute("CREATE INDEX fast_unix_sentiment ON %s(UnixTime, Polarity)" % (self.tableName))
            conn.commit()
            conn.close()
            return(True)
        except Exception as e:
            print(str(type(e)) + ": " + str(e))
            return(False)


    def run(self):
        if len(self.keyWords)>0:
             try:
                 auth = OAuthHandler(self.ckey, self.csecret)
                 auth.set_access_token(self.atoken, self.asecret)

                 api = API(auth)

                 # If the authentication was successful, you should
                 # see the name of the account print out
                 print("Authorization: " + str(api.me().name))

                 twitterStream = Stream(auth, listener(self, dbName=self.dbName, tableName=self.tableName))
                 twitterStream.filter(track=self.keyWords, is_async =True)

                 #time.sleep(0.5)
             except Exception as e:
                 print(str(type(e)) + ": " + str(e))
                 time.sleep(5)
        else:
            print("No Keywords to track!")
