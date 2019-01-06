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
from TweetsProcessing import TweetsProcessing
from Config import RunConfig
from subprocess import call


def thread_second():
    call(["python", "dashStreamMain.py"])



def main():

    ckey = RunConfig.ckey
    csecret = RunConfig.csecret
    atoken = RunConfig.atoken
    asecret = RunConfig.asecret
    dbName = RunConfig.dbName
    tableName = RunConfig.tableName
    keyWords= RunConfig.keyWords

    tweetsProcessing = TweetsProcessing(ckey=ckey, csecret=csecret, atoken=atoken, \
                                        asecret=asecret, dbName=dbName, tableName=tableName, keyWords=keyWords)


    tweetsProcessing.createTwitterDB()
    tweetsProcessing.run()
    print("Twitter connection success!")

    processThread = Thread(target=thread_second)  # <- note extra ','
    processThread.daemon = True
    processThread.start()
    print("Create web dash!")



if __name__ == '__main__':
    main()
