#!/bin/bash

username=masayuki
path=local/bitcoin_twitter_analysis/textmining
echo $1
source ~/.bashrc
python2.7 /Users/${username}/${path}/replace_main_bitcoin.py $1
python2.7 /Users/${username}/${path}/main_$1.py 
./count.sh $1
