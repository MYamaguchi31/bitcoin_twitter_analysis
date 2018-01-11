#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import commands
from datetime import datetime
import time
cmdP = '''mongo localhost:27017/bitcoin --eval 'db.tweets_text.find({$and:[{text: /BTC/i },{created_at:{$lt:timeP}}]}).count()' --quiet'''
cmdN = '''mongo localhost:27017/bitcoin --eval 'db.tweets_text.find({text: /hogehoge/i }).count()' --quiet'''

#countN = commands.getoutput('''mongo localhost:27017/bitcoin --eval 'db.tweets_text.find({text: /BTC/i }).count( function(){ return new Date(this.created_at) > new Date("2018/01/08 22:17:43"); })' --quiet''')

countP = commands.getoutput(cmdP)
countN = commands.getoutput(cmdN)
date=datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
rate = float(countN)/float(countP)
if float(countP)==0. or rate<=1.:
    print 'no-data'
else:
    print '{0}:{1}:_{2}_percent'.format(date,"hogehoge",rate)
