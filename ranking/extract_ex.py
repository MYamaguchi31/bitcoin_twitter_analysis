import re
a = '<a>'
b = '<b>'

text = '<a>bbb<b>ccc<b>'
r = re.search(r'%s(.*?)%s'%(a,b), text)

print(r.group(1))
