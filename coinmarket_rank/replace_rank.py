# coding: UTF-8
import sys
import os
import re
#文字コード指定に必要
import codecs

#置換文字列を指定
name_old='tab' #この文字を含むファイルを操作＋ファイル名の置換元文字列
name_new='txt' #ファイル名の置換後文字列
txt_old='\n' #ファイル内の置換元 文字列
txt_new= ' OR ' #ファイル内の置換後文字列

#パス指定小楽でスクリプト配置フォルダのファイル一覧取得
files = os.listdir("./")
count=0
for file in files:
    txt = re.compile("rank.tab")
    if txt.search(file):
        # ファイル名の置換前後の文字列を指定
        file_new = file.replace(name_old,name_new)
        
        read_file = codecs.open(file, 'r', 'utf-8')
        write_file = codecs.open(file_new, 'w', 'utf-8')

        lines = read_file.readlines() #読み込み
        lines2 = []
        for line in lines:
            if count<300: 
                line = line.replace(txt_old,txt_new) #テキスト置換
            elif count==300:
                line = line.replace(txt_old,'') #テキスト置換
            if count>300: 
                continue
            count+=1
            lines2.append(line) #別リストにする
        else:
            write_file.write(''.join(lines2)) #書き込み
            read_file.close()

    else:
        pass
