path=/Users/masayuki/local/bitcoin_twitter_analysis/trading_exchanges
while read line
do
wget -k -p -nH -N --html-extension  -U ""  https://www.coingecko.com/en/coins/$line/trading_exchanges#panel  
echo $line >> trading_list.tab
grep ex-coin  ./en/coins/$line/trading_exchanges.html >> trading_list.tab
done < ${path}/list.tab

