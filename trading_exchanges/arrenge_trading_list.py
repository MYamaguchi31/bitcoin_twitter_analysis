
f = open('./trading_list.dat')
line = f.readline()
dic={}
value="test"
while line:
    if(line=="Exchange\n"):
        #dic.pop(line, None)
        dic.pop(key, None)
        value = key
        line = f.readline()
        continue
    key = line.replace('\n','')
    dic.setdefault(key, set()).add(value)
    line = f.readline()
    
#print dic['Bitflyer']
for key, value in dic.iteritems():
    print key, value

f.close()
