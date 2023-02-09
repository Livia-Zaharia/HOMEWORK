# 5. Perfect Numbers1
# : An integer, n, is said to be perfect when the sum of all of the proper
# divisors of n is equal to n. For example, 28 is a perfect number because its proper
# divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28. Write a function that
# determines whether or not a positive integer is perfect. Your function will take one
# parameter. If that parameter is a perfect number then your function will return true.
# Otherwise it will return false. In addition, write a main program that uses your function
# to identify and display all of the perfect numbers between 1 and 10,000. Import your
# solution to Exercise 4 when completing this task.
# Hint: You can use the built-in function sum(foo) where foo is a list to get the sum
# of its elements. Use the result of the function that returns the list of proper divisors
# and sum its elements to check against the numbers going from 1 to 10,000.
# Don't forget to use the main() function when building your programs!

from proper_divisors import proper

def perfect (no:int)->bool:
    if no == sum(proper(no)):
        return True
    else:
        return False


def main():
    # no=int(input("no:"))
    # print(perfect(no))
    no_list=[]
    for i in range(1,10001):
        if perfect(i):
            no_list.append(i)
    
    print(no_list)


if __name__ == "__main__":
    main()