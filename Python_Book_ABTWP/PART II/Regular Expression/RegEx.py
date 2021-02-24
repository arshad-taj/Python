import re
s = "-6/4"
a = re.match('^[-+]?[0-9]*[.][0-9]+$',s)
print(a)
print(bool(a))

