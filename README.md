# Live-Twitter-Sentiment-App

Uses live streamed twitter tweets filtered by your own kwy words, to make sentiment analysis to classify on positve and negative tweets. 
Store them in local database, and then creates a dashbord with live charts.

### Availble:
* Historical scatter chart. With dynamic historical window size.
* Pie chart, which shows positive/negative partition. Also availble to control historical period.
* Live table with tweets.
* Possible to change list of 'key words', in Config.py

For using neccessary to have your own ckey, csecret, atoken, asecret for connection to twitter.
Fill them in Config.py
For this neccassary to create your own dev account. https://developer.twitter.com/en/account/get-started

<hr>

### Requiremets:
* python 3.6
* pandas
* threading
* sqlite3
* textblob
* tweepy
* plotly
* dash
* dash-html-components
* dash-core-components

### Install such releases:
```
pip install dash==0.34.0  # The core dash backend
pip install dash-html-components==0.13.4  # HTML components
pip install dash-core-components==0.41.0  # Supercharged components
```

### Usage:
Double click on run.bat
![alt text](https://user-images.githubusercontent.com/10981310/50736017-06fabf00-11c0-11e9-9ca8-a2191f08cad8.PNG)

<hr>

### Live dashboard example:
![alt text](https://user-images.githubusercontent.com/10981310/50736060-b46dd280-11c0-11e9-835c-b9e377071f08.PNG)
![alt text](https://user-images.githubusercontent.com/10981310/50736066-dff0bd00-11c0-11e9-81f6-1f4c76162d5a.PNG)
