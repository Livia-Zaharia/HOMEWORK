"""
2. Count the Elements1
: Python’s standard library includes a method named count that
determines how many times a specific value occurs in a list. In this exercise, you will create a
new function named count_range which determines and returns the number of elements
within a list that are greater than or equal to some minimum value and less than some
maximum value. Your function will take three parameters: the list, the minimum value and
the maximum value. It will return an integer result greater than or equal to 0. Include a main
program that demonstrates your function for several different lists, minimum values and
maximum values. Ensure that your program works correctly for both lists of integers and
lists of floating point numbers.

"""
import random

def count_range(data:list,max:int|float,min:int|float)->int:
    count=0
    for item in data:
        if item>=min and item<max:
            count+=1

    return count


def main():
    data_int=[]
    for i in range(1000):
        data_int.append(i)

    data_float=[]
    for i in range(1000):
        data_float.append(round(i*0.1,2))

    if (random.randint(0,100))%2:
       data=random.sample(data_int,10)
    else:
       data=random.sample(data_float,10)

    for i in data:
        print(i)

    max=float(input("max value "))
    min=float(input("min value "))
    print(count_range(data,max,min))

          


       

if __name__=="__main__":
    main()