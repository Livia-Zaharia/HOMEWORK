
# 8. The Collatz Sequence2
# : Write a function named collatz() that has one parameter named
# number. If number is even, then collatz() should print number // 2 and return this
# value. If number is odd, then collatz() should print and return 3 * number + 1 . Then
# write a program that lets the user type in an integer and that keeps calling collatz() on
# that number until the function returns the value 1. (Amazingly enough, this sequence
# actually works for any integer — sooner or later, using this sequence, you’ll arrive at 1! Even
# mathematicians aren’t sure why. Your program is exploring what’s called the Collatz
# sequence, sometimes called “the simplest impossible math problem.”) Remember to convert
# the return value from input() to an integer with the int() function; otherwise, it will be a
# string value.
# Hint: The output of this program could look something like this:
# Enter number: 3105168421

def collatz(number: int) ->int:
    if number%2 ==0:
        print (number//2)
        return number//2
    else:
        print (1+(number*3))
        return (1+(number*3))
    

no=int(input("Number to start the collatz sequence "))
d=collatz(no)
while d!=1:
    d=collatz(d)
