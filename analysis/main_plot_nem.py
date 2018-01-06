#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# data.txt からデータを読み込んで配列にする
#data = np.loadtxt("/Users/masayuki/local/bitcoin/textmining/tab/nem.tab")
data = np.loadtxt("/Users/masayuki/local/bitcoin/textmining/tab/nem.tab")
diff = np.diff(data)

plt.plot(diff)
#plt.show()
filename = "./png/nem.png"
plt.savefig(filename)
