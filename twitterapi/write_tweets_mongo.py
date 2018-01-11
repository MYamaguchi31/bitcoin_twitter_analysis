# -*- coding: utf-8 -*-
 
from pymongo import MongoClient
from search_tweet import TweetsGetter
 
client = MongoClient('localhost', 27017)
 
db = client.bitcoin
search_word = "%s" % "u'hogehoge'"
tweets = TweetsGetter.bySearch(search_word).collect(total=1000)
for tweet in tweets:
    tweet2 = {}
    #tweet2['id'] = tweet['id']
    tweet2['text'] = tweet['text']
    tweet2['created_at'] = tweet['created_at']
    #tweet2['user'] = {'screen_name' : tweet['user']['screen_name']}
    
    #create_time = tweet['created_at']
    #tweet2['created_at'] = date('Y-m-d H:i:s', strtotime(create_time));
    db.tweets_text.insert(tweet2)
