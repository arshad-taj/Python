"""
The Collatz Sequence:

Write a function named collatz() that has one parameter named number . If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1 .
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1 .
(Amazingly enough, this sequence actually works for any integer—sooner
or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
sure why. Your program is exploring what’s called the Collatz sequence, some-
times called “the simplest impossible math problem.”)

"""


def collatz_fun(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


result = None

while result!=1:
    try:
        result = collatz_fun(int(input('Enter Number > ')))
        print(result)
    except ValueError:
        print("Type numbers only")
