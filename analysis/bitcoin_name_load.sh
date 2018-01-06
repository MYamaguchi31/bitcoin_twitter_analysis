#!/bin/bash

path=/Users/masayuki/local/bitcoin_twitter_analysis/coinmarket_rank

while read line
do
   echo $line
   #plot.sh $line &
done < ${path}/rank.tab
