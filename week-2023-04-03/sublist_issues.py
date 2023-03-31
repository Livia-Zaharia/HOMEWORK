"""
3. Does a List contain a Sublist?1
: A sublist is a list that makes up part of a larger list. A sublist
may be a list containing a single element, multiple elements, or even no elements at all. For
example, [1], [2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a sublist of [1, 2,
3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because the elements 2 and 4 are not adjacent in the
longer list. The empty list is a sublist of any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is
a sublist of itself, meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4]. In this exercise you
will create a function, is_sublist , that determines whether or not one list is a sublist of
another. Your function should take two lists, larger and smaller, as its only parameters. It
should return True if and only if smaller is a sublist of larger. Write a main program that
demonstrates your function.

"""
import random


def is_sublist(larger:list, smaller:list)->bool:
    A=""
    B=""
   
    for item in larger:
        A+=str(item)
        A+="."

    for item in smaller:
        B+=str(item)
        B+="."

    if A.find(B)!=-1:
        return True
    return False


def main():
    data_int=[]
    for i in range(100):
        data_int.append(i)

    data=random.sample(data_int,10)
    
    for i in data:
        print(i)
    
    to_check=[]
    for i in range(4):
         to_check.append(int(input("no in list to check ")))
        
    print(is_sublist(data,to_check))

                

if __name__=="__main__":
    main()