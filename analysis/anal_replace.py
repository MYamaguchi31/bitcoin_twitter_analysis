# coding: UTF-8
import sys
import os
import re
#文字コード指定に必要
import codecs
#from datetime import datetime
import datetime,time

args = sys.argv
coinname = args[1]

timeP =  datetime.datetime.now() - datetime.timedelta(hours=12)
unixtimeP = str(int(time.mktime(timeP.timetuple())))

print unixtimeP
#str_timeP = timeP.strftime('%Y/%m/%d %H:%M:%S')

#置換文字列を指定
name_old =  'anal'      #この文字を含むファイルを操作＋ファイル名の置換元文字列
name_new =  'anal_sub'  #ファイル名の置換後文字列
txt_old1  =  'hogehoge'  #ファイル内の置換元 文字列
txt_new1  =  coinname    #ファイル内の置換後文字列
txt_old2  = 'timeP'     #ファイル内の置換元 文字列
txt_new2  = unixtimeP       #ファイル内の置換後文字列


#パス指定小楽でスクリプト配置フォルダのファイル一覧取得
files = os.listdir("./")
for file in files:
    txt = re.compile("anal.py")
    if txt.search(file):
        # ファイル名の置換前後の文字列を指定
        file_new = file.replace(name_old,name_new)
        
        read_file = codecs.open(file, 'r', 'utf-8')
        write_file = codecs.open(file_new, 'w', 'utf-8')
        
        lines = read_file.readlines() #読み込み
        lines2 = []
        for line in lines:
            line = line.replace(txt_old1,txt_new1) #テキスト置換
            line = line.replace(txt_old2,txt_new2) #テキスト置換
            
            lines2.append(line) #別リストにする
        else:
            write_file.write(''.join(lines2)) #書き込み
            read_file.close()
    else:
        pass
