#!/user/bin/env python2.7
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
import requests
import time, calendar
import sys, codecs

#word = raw_input(u"input: ")
word = u"input: emacs"

C_KEY = '4gjrfoldzln6sHGieBZQqlDbl'
C_SECRET = '1f3EsoBJ3kXWkmmiu3CEJyX9pmkExYPC4rLGgdMV9WPTrotlq1'
A_TOKEN = '949230339053899776-2J64QJvoFwnYZhSQUwFoQDBx4o0rrmC'
T_SECRET = 'KwsUk73LEDP44TRjxD4f7g9caSGabAHbMeFTjPc5AzbZ6'


URL = "https://stream.twitter.com/1.1/statuses/filter.json"

def Client_key():
    return OAuth1Session(C_KEY,
        client_secret = C_SECRET,
        resource_owner_key = A_TOKEN,
        resource_owner_secret = T_SECRET
    )

def Response(client, **filter_data):
    return client.post(
        URL,
        data = filter_data,
        stream = True
    )


def YmdHMS(created_at):
    time_utc = time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    unix_time = calendar.timegm(time_utc)
    time_local = time.localtime(unix_time)
    return int(time.strftime("%Y%m%d%H%M%S", time_local))

def Print_l(r): 
    for line in r.iter_lines():
        print("test3")
        stream = line.decode("utf-8")
        #tweet = json.loads(line)
        tweet = json.loads(stream)
        print("test4")
        Created_at = YmdHMS(tweet["created_at"])
        User = (tweet["user"]["screen_name"].encode("utf-8"))
        Name = (tweet["user"]["name"].encode("utf-8"))
        Text = (tweet["text"].encode("utf-8"))

        try:
            if tweet["user"]["lang"] == "ja":
                print("本文:%s",Text)
        except:
            pass

if __name__ == "__main__":
    client = Client_key()
    print("test1")
    r = Response(client, track=word)
    print("test2")
    Print_l(r)
    print("test10")
