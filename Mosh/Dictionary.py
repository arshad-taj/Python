numDict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}

ip = input('Phone :')

for i in ip:
    print(numDict[int(i)], end=" ")
