def gen():
    yield 5
    a= 5+5
    yield a
    z = 5**3
    yield z
v = gen()

for i in v:
    print(i)