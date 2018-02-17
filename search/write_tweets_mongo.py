# -*- coding: utf-8 -*-
 
from pymongo import MongoClient
from search_tweet import TweetsGetter
import datetime, time ,pytz


client = MongoClient('localhost', 27017)
db = client.bitcoin
tweets = TweetsGetter.bySearch(u'hogehoge').collect(total=30000)
#tweets = TweetsGetter.bySearch(u'hogehoge').collect(total=100)

def str_to_date(str_date):
    #base_data = str_date
    #date_time = time.strptime(base_data, "%b %d %H:%M:%S %Y GMT")
    #unix_time = int(time.mktime(date_time))
    dts = datetime.datetime.strptime(str_date,'%a %b %d %H:%M:%S +0000 %Y')
    dtu = pytz.utc.localize(dts).astimezone(pytz.timezone('UTC'))
    unix_time = int(time.mktime(dtu.timetuple()))
    return unix_time

if __name__ == '__main__':
    for tweet in tweets:
        tweet2 = {}
    #tweet2['id'] = tweet['id']
        tweet2['text'] = tweet['text']
        tweet2['created_at'] = str_to_date(tweet['created_at'])
    #tweet2['user'] = {'screen_name' : tweet['user']['screen_name']}
    #create_time = tweet['created_at']
    #tweet2['created_at'] = date('Y-m-d H:i:s', strtotime(create_time));
        db.tweets_text.insert(tweet2)
