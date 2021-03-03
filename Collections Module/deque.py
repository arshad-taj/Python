#it is like list but items cn be added/removed  from the both ends
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(5)
print(d)

d.extend(a for a in range(6,10))
print(d)

d.extendleft([11,22,33])
print(d)

d.rotate(2)
d.rotate(-3)