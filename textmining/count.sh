#!/bin/bash
source ~/.bashrc
cmd="mongo localhost:27017/bitcoin --eval 'db.tweetdata.find({text: /hogehoge/i }).count()' --quiet  >> ./tab/hogehoge.txt"
while read line
do
    eval ${cmd//hogehoge/$line}
done < /Users/masayuki/local/bitcoin_twitter_analysis/coinmarket_rank/rank_demo.tab


