import requests
from requests_oauthlib import OAuth1

api_key = '4gjrfoldzln6sHGieBZQqlDbl'
api_secret = '1f3EsoBJ3kXWkmmiu3CEJyX9pmkExYPC4rLGgdMV9WPTrotlq1'
access_token = '949230339053899776-2J64QJvoFwnYZhSQUwFoQDBx4o0rrmC'
access_secret = 'KwsUk73LEDP44TRjxD4f7g9caSGabAHbMeFTjPc5AzbZ6'

url = "https://stream.twitter.com/1.1/statuses/filter.json"
#url = "https://stream.twitter.com/1.1/search/tweets.json"

auth = OAuth1(api_key, api_secret, access_token, access_secret)
print("test1")
#r = requests.post(url, auth=auth, stream=True, data={"follow":"nasa9084","track":"emacs"})
r = requests.post(url, auth=auth, stream=True, data={"follow":"31bit","track":"emacs"})
print("test2")
for line in r.iter_lines():
  print("test3")
  if not list:
    print("null")
  print(line["text"])  
print("test4")
