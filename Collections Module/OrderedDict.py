#remembers the order in which the items are inserted

from collections import OrderedDict
dict1  = OrderedDict()
dict1['a'] = 1
dict1['b'] = 11
dict1['c'] = 111
dict1['d'] = 1111


print(dict1)

print(dict(dict1))

