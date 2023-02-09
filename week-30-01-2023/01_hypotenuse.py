# 1. Compute the Hypotenuse1
# : Write a function that takes the lengths of the two shorter sides
# of a right triangle as its parameters. Return the hypotenuse of the triangle, computed using
# Pythagorean theorem, as the function’s result. Read the lengths of the shorter sides of a
# right triangle from the user and use your function to compute the length of the hypotenuse,
# and display the result.

import math

def hypotenuse(side1: float, side2: float) -> float:
    side3=math.sqrt(math.pow(side1,2)+math.pow(side2,2))
    return side3

side1=float(input("side1: "))
side2=float(input("side2: "))

print("then side3 must be", hypotenuse(side1, side2))