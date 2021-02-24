from functools import reduce
x = [0,1]
y = [0,1]
z = [0,1,2]

l=[]
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            l.append([i,j,k])
print(l)
count = 0
while count!=len(l)-1:

    sum = reduce(lambda a,b:a+b,l[count])
    if sum==3:
        del l[count]
    else:
        count+=1

print('***************************************************************')
print(l)
