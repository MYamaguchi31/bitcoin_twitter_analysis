#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# data.txt からデータを読み込んで配列にする
#data = np.loadtxt("/Users/masayuki/local/bitcoin/textmining/tab/nem.tab")
data = np.loadtxt("/Users/masayuki/local/bitcoin_twitter_analysis/textmining/tab/Bitcoin.tab")
diff = np.diff(data)

plt.plot(diff)
#plt.show()
filename = "./png/Bitcoin.png"
plt.savefig(filename)
