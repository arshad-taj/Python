lst = [4, 4, 5, 5, 5, 3, 8, 88, 9, 9, 4]
unique_list = []

for i in lst:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

