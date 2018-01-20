for i in `seq 1 11`
do
    wget -k -p -nH -N --html-extension  -U ""  https://www.coingecko.com/en?page=$i
    grep "www.coingecko.com/en/coins" en\?page\=$i.html  >> list.dat    
done
rm *.html