# 6. Next Prime1
# : In this exercise you will create a function named next_prime that finds and
# returns the first prime number larger than some integer, n. The value of n will be passed to
# the function as its only parameter. Write a program that reads an integer from the user and
# displays the first prime number larger than the entered value. Ideally, import and use your
# solution to Exercise 5 while completing this exercise.


import is_prime

def next_number(no: int) ->int:
    while True:
        no=no+1
        if is_prime.prime(no):
            return no

no=int(input("Number to check for next prime of: "))
print("so next prime will be...", next_number(no))


