"""
1. Convert an Integer to its Ordinal Number1
: Words like first, second and third are referred
to as ordinal numbers. In this exercise, you will write a function that takes an integer as its
only parameter and returns a string containing the appropriate English ordinal number as its
only result. Your function must handle the integers between 1 and 12 (inclusive). It should
return an empty string if a value outside of this range is provided as a parameter. Include a
main program that demonstrates your function by displaying each integer from 1 to 12 and
its ordinal number.

"""

def ordinal_name(number)->str:
    ordinals=["first","second","third","fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    if number<=12:
        return ordinals[number-1]
    else:
        return "+"



def main():
    number=int(input("date to be converted into ordinal numeral "))
    print(ordinal_name(number))



if __name__=="__main__":
    main()