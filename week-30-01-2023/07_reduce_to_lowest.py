
# 7. Reduce a Fraction to Lowest Terms1
# : Write a function that takes two positive integers that
# represent the numerator and denominator of a fraction as its only two parameters. The
# body of the function should reduce the fraction to lowest terms and then prints both the
# numerator and denominator of the reduced fraction For example, if the parameters passed
# to the function are 6 and 63 then the function should print 2 and 21. Write a program that
# allows the user to enter a numerator and denominator. Then your program should display
# the reduced fraction.
# Hint: In the past we wrote a program for computing the greatest common divisor of
# two positive integers. You may find that code useful when completing this exercise.

import is_prime


def greatest_common_divisor(no_1: int, no_2:int) ->int:
    if is_prime.prime(no_1) and is_prime.prime(no_2) and no_1!=no_2:
        return 0
    elif is_prime.prime(no_1) and is_prime.prime(no_2) and no_1==no_2:
        return no_1
    elif is_prime.prime(no_1) or is_prime.prime(no_2):
        return 0
    else:    
        if no_1<no_2:
            d=no_1
        else:
            d=no_2
        while no_1%d !=0 or no_2%d !=0:
            d=d-1
        if d!=0:
            return d


no_1=int(input("specify first number: "))
no_2=int(input("specify second number: "))
print( no_1, "/", no_2)
div=greatest_common_divisor(no_1, no_2)
if div!=0:
    print(no_1//div, "/", no_2//div)
else:
    print("Those numbers are prime between themselves")
