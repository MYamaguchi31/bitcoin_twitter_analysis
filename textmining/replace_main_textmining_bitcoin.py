# coding: UTF-8
import sys
import os
import re
#文字コード指定に必要
import codecs

args = sys.argv
#f = open('/Users/masayuki/local/bitcoin_twitter_analysis/coinmarket_rank/rank.txt')
f = open('/Users/masayuki/local/bitcoin_twitter_analysis/coinmarket_rank/rank_demo.txt')
lines = f.read()
f.close()


#置換文字列を指定
name_old='main_textmining' #この文字を含むファイルを操作＋ファイル名の置換元文字列
name_new='main_textmining_sub' #ファイル名の置換後文字列
txt_old='hogehoge' #ファイル内の置換元 文字列
txt_new= 'u'+'"'+lines.replace('\n','')+'"'; #ファイル内の置換後文字列

#パス指定小楽でスクリプト配置フォルダのファイル一覧取得
files = os.listdir("./")
for file in files:
    txt = re.compile("main_textmining.py")
    if txt.search(file):
        # ファイル名の置換前後の文字列を指定
        file_new = file.replace(name_old,name_new)
        
        read_file = codecs.open(file, 'r', 'utf-8')
        write_file = codecs.open(file_new, 'w', 'utf-8')

        lines = read_file.readlines() #読み込み
        lines2 = []
        for line in lines:
            line = line.replace(txt_old,txt_new) #テキスト置換
            lines2.append(line) #別リストにする
        else:
            write_file.write(''.join(lines2)) #書き込み
            read_file.close()

#       os.rename(file, file_new)
    else:
        pass
