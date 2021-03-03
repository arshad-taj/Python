# Counter is a method from collections module
# It returns dictionary with given elemenets as keys and their count as values

from collections import Counter
a = 'abde'
b = 'abbbbbcccccccccddeee'
char_counter = Counter(b)
print(f'Counts dictionary --> {char_counter}')

print(f'most common --> {char_counter.most_common(2)}') #it'll give most repeated character
                                                        #it'll return list of tuples
print(f'list of elements --> {list(char_counter.elements())}')


