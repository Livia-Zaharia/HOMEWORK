
# 4. List of Proper Divisors1
# : A proper divisor of a positive integer, n, is a positive integer less
# than n which divides evenly into n. Write a function that computes all of the proper
# divisors of a positive integer. The integer will be passed to the function as its only
# parameter. The function will return a list containing all of the proper divisors as its only
# result. Complete this exercise by writing a main program that demonstrates the function
# by reading a value from the user and displaying the list of its proper divisors.
# Hint: You can search for the proper divisor in a loop and append each divisor to a
# result list and return it at the end of the function.

def proper(no:int)->list:
    divisors=[]
    for i in range (1,(no//2)+1):
        if no%i == 0:
            divisors.append(i)
    
     
    return divisors


def main():
    no=int(input("Number to be checked: "))
    print(proper(no))

if __name__ == "__main__":
    main()