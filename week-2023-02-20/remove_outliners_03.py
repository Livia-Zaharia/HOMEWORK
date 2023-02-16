"""
3. Remove Outliers1
: When analyzing data collected as part of a science experiment it may be
desirable to remove the most extreme values before performing other calculations. Write a
function that takes a list of values and an non-negative integer, n, as its parameters. The
function should create a new copy of the list with the n largest elements and the n smallest
elements removed. Then it should return the new copy of the list as the function’s only
result. The order of the elements in the returned list does not have to match the order of the
elements in the original list. Write a main program that demonstrates your function. Your
function should read a list of numbers from the user and remove the two largest and two
smallest values from it. Display the list with the outliers removed, followed by the original
list. Your program should generate an appropriate error message if the user enters less than

"""

import copy

def check_and_eliminate():
    if len (no_list)<=2*no_elements:
        return False
    else:
        global no_list_copy
        no_list_copy=copy.copy(no_list)
        no_list_copy.sort()
        no_list_copy=no_list_copy[no_elements:-no_elements]
        return True

def read():
    global no_list
    no_list=[]
    while True:
        no=input("New value you want in: ")
        if no=="":
            break
        no_list.append(int(no))

def main():
    read()
    global no_elements
    no_elements=int(input("How many outliners to be removed: "))
    if check_and_eliminate():
        for element in no_list_copy:
            print(element)
        print("+++++++++++++++")
        for element in no_list:
            print(element)
    else:
        print("List was too short")

if __name__=="__main__":
    main()