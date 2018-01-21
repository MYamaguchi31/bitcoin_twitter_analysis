for i in `seq 1 11`
do
    wget -k -p -nH -N --html-extension  -U ""  https://www.coingecko.com/en?page=$i
    python2.7 list_marcket_cap.py $i
    #grep "www.coingecko.com/en/coins" en\?page\=$i.html  >> list.dat    
done

rm -rf *.html robots.txt ./assets favicon.ico
