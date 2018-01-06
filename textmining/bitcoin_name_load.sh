#!/bin/bash

path=/Users/masayuki/local/bitcoin_twitter_analysis/coinmarket_rank

while read line
do
   echo $line
   #twitter_ana.sh $line &
done < ${path}/rank.tab
