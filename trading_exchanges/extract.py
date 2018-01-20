import re

a = '<a href="https://www.coingecko.com/en/coins/'
b = '">'
f = open('./list.dat')

line = f.readline()
g = open('./list.tab', 'w')
count=0

while line:
    r = re.search(r'%s(.*?)%s'%(a,b), line)    
    #if count>=40: 
    #    break
    g.write(r.group(1))
    g.write('\n')
    line = f.readline()
    count+=1
f.close()



