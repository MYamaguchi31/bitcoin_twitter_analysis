import re

a = '/">'
b = '</a></span>'
f = open('./rank.log')

line = f.readline()
g = open('./rank.tab', 'w')

while line:
    r = re.search(r'%s(.*?)%s'%(a,b), line)    
    #print r.group(1)
    g.write(r.group(1))
    g.write('\n')
    line = f.readline()
f.close()



