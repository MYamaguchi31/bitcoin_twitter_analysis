#!/bin/bash
source ~/.bashrc
mongo localhost:27017/$1 --eval 'db.tweetdata.count()' --quiet >> ./tab/$1.tab
