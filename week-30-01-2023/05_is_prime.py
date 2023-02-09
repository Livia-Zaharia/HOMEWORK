
# 5. Is a Number Prime?1
# : A prime number is an integer greater than 1 that is only divisible by
# one and itself. Write a function that determines whether or not its parameter is prime,
# returning True if it is, and False otherwise. Write a program that reads an integer from the
# user and displays a message indicating whether or not it is prime.

def prime(no: int) ->bool:
    i=2
    if no==0:
        return False
    else:
        while i<no:
            if no%i==0:
                return False
            
            return True
        
no=int(input("Number to check for prime-ness: "))
if prime(no):
    print("It is prime")
else:
    print("It is not prime")