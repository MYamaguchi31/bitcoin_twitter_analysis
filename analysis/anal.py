#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import commands
cmdP = '''mongo localhost:27017/bitcoin --eval 'db.tweets_text.find({$and:[{text: /BTC/i },{created_at:{$lt:timeP}}]}).count()' --quiet'''
cmdN = '''mongo localhost:27017/bitcoin --eval 'db.tweets_text.find({text: /hogehoge/i }).count()' --quiet'''

#countN = commands.getoutput('''mongo localhost:27017/bitcoin --eval 'db.tweets_text.find({text: /BTC/i }).count( function(){ return new Date(this.created_at) > new Date("2018/01/08 22:17:43"); })' --quiet''')

countP = commands.getoutput(cmdP)
countN = commands.getoutput(cmdN)
print countP
print countN
