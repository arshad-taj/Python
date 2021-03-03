a= [1,2,3,4]
print(list(map(lambda f:f*f,a)))
def square(x):
    return  x*x

print(list(map(square,a)))