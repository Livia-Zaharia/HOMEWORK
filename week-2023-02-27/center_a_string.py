"""
3. Center a String in the Terminal1
: Write a function that takes a string of characters as its
first parameter, and the width of the terminal in characters as its second parameter. Your
function should return a new string that consists of the original string and the correct
number of leading spaces so that the original string will appear centered within the provided
width when it is printed.
"""


def main():
    text=input("what do you want centered: ")
    number=int(input("width of characters of terminal "))
    print(text.center(number,"+"))



if __name__=="__main__":
    main()