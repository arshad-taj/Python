numbers = [5, 54, 88, 63, 7]
largest_num = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest_num:
        largest_num = numbers[i]

print(f'Largers num is : {largest_num}')

num = numbers
print(num)