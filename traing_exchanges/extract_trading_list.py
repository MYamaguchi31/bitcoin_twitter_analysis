import re
#<th class="ex-coin">Exchange</th>

f = open('./trading_list.tab')
line = f.readline()
g = open('./trading_list.dat', 'w')
count=0

while line:
    #r = re.search(r'%s(.*?)%s'%(a,b), line)    
    r1 = line.replace('<th class="ex-coin">','')
    r2 = r1.replace('</th>','')
    r3 = r2.replace('<td class="ex-coin">','')
    r4 = r3.replace('</td>','')
    g.write(r4)
    #g.write('\n')
    line = f.readline()
f.close()



