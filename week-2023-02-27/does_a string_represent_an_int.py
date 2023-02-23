"""
5. Does a String Represent an Integer?1
: In this exercise you will write a function named
is_integer that determines whether or not the characters in a string represent a valid
integer. When determining if a string represents an integer you should ignore any leading or
trailing white space. Once this white space is ignored, a string represents an integer if its
length is at least 1 and it only contains digits, or if its first character is either + or - and the
first character is followed by one or more characters, all of which are digits. Write a main
program that reads a string from the user and reports whether or not it represents an
integer.
Hint: You may find the lstrip , rstrip and/or strip methods for strings helpful
when completing this exercise. Documentation for these methods is available online.

"""

def is_integer(text):
    text=text.strip(" ")
    if text[0]=="+" or text[0]=="-" or text[0].isdigit():
        if text[1:].isdigit():
            return True
    return False


def main():
    number=input("string to be checked: ")
    if is_integer(number):
        print("ït was an integer after all")
    else:
        print("it was not an integer")




if __name__=="__main__":
    main()