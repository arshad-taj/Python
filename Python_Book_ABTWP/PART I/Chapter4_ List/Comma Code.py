lst = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list_arg):
    s = ''
    for i in lst:
        if i == lst[len(lst) - 1]:
            s = s + 'and ' + i
        else:
            s = s + i + ' ,'
    return s

print(comma_code(lst))
