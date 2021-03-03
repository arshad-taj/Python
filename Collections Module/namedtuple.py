from collections import namedtuple

Point = namedtuple('Point','x,y')
pt = Point('dddd',8)
print(pt.x)
print(pt.y)