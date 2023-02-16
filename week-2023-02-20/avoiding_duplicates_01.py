"""
1. Avoiding Duplicates1
: In this exercise, you will create a program that reads words from the
user until the user enters a blank line. After the user enters a blank line your program should
display each word entered by the user exactly once. The words should be displayed in the
same order that they were entered. For example, if the user enters:
first second first third second
then your program should display:
first second third
Hint: You can check if a word already exists in the list before appending it.

"""

def check_not_exist(word)->bool:
    if word in word_list:
        return False
    else:
        return True

def read_write():
    global word_list
    word_list=[]
    while True:
        word=input("New word you want in: ")
        if word=="":
            break
        if check_not_exist(word):
            word_list.append(word)

def main():
    read_write()
    for element in word_list:
        print(element)

if __name__=="__main__":
    main()