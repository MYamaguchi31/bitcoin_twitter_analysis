#!/bin/bash

path=/Users/masayuki/local/bitcoin_twitter_analysis/ranking

while read line
do
    #echo $line
    python2.7 anal_replace.py $line
    rate=`python2.7 anal_sub.py`
    
    if [ ${rate} = "no-data" ]; then
	echo "no-data"	
    else
	python2.7 post_tweet.py ${rate}
    fi
done < ${path}/rank.tab
