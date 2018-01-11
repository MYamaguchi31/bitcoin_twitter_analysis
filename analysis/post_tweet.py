# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

CK = '4gjrfoldzln6sHGieBZQqlDbl'                              # Consumer Key
CS = '1f3EsoBJ3kXWkmmiu3CEJyX9pmkExYPC4rLGgdMV9WPTrotlq1'     # Consumer Secret
AT = '949230339053899776-2J64QJvoFwnYZhSQUwFoQDBx4o0rrmC'     # Access Token
AS = 'KwsUk73LEDP44TRjxD4f7g9caSGabAHbMeFTjPc5AzbZ6'          # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
alert = "Hello, World!"
params = {"status": alert}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
