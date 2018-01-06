#!/bin/bash
wget -k -p -nH -N --html-extension  -U ""  https://coinmarketcap.com/all/views/all
grep currency-symbol ./all/views/all/index.html > rank.log
python2.7 extract.py
