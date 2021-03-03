from functools import reduce

nums = [2, 6, 5, 4, 5, 5, 8, 7, 9, 4, 5, 6, 2, 2, 6, 3, 3, 5, 5, 5, 8, 8]

even_nums = list(filter(lambda n: n % 2 == 0, nums))  # filtering the even from list nums
print(f'Even numbers: {even_nums}')

doubles = list(map(lambda n: n * 2, even_nums))  # doubling all numbers from even_nums
print(f'Doubls : {doubles}')

sum = reduce(lambda a, b: a + b, doubles)
print(sum)
print(type(sum))



