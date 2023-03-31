"""
4. Generate All Sublists of a List1
: Using the definition of a sublist from Exercise 3, write a
function that returns a list containing every possible sublist of a list. For example, the sublists
of [1, 2, 3] are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your function will always
return a list containing at least the empty list because the empty list is a sublist of every list.
Include a main program that demonstrate your function by displaying all of the sublists of
several different lists.

"""

import random


def all_sublist(data:list,no:int)->list:
    i=0
    j=no
    sublists=[]
    while(i<no):
        while(j>i):
            sublists.append(data[i:j])
            j=j-1
        i=i+1
        j=no
    
    sublists.append([])
    return sublists

 


def main():
    data_int=[]
    for i in range(100):
        data_int.append(i)

    data=random.sample(data_int,3)
    
    for i in data:
        print(i)

    last_list=all_sublist(data, len(data))
    print(last_list)
    for item in (last_list):
        print(item)

                

if __name__=="__main__":
    main()