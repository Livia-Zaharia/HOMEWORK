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