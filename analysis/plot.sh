#!/bin/bash

python2.7 replace_main_bitcoin.py $1
python3.6 main_plot_$1.py
