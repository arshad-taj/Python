#it will return default value if key doesn't exist
from collections import defaultdict

d = defaultdict(int)  # need to specify default data type
print(d['c']) # key 'c' doesn't exist in dictionary d


d2 = defaultdict(float)
print(d2[4]) # key 4 doesn't exist in dictionary d2

d3 = defaultdict(list)
print(d3['DD']) # key 'DD' doesn't exist in dictionary d2

