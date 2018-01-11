import re

a = '/">'
b = '</a></span>'
f = open('./rank.log')

line = f.readline()
g = open('./rank.tab', 'w')
count=0

while line:
    r = re.search(r'%s(.*?)%s'%(a,b), line)    
    if count>=40: 
        break
    #g.write('$')
    g.write(r.group(1))
    #g.write('"')
    g.write('\n')
    line = f.readline()
    count+=1
f.close()



