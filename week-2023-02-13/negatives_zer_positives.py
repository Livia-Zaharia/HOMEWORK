# 3. Negatives, Zeros and Positives1
# : Create a program that reads integers from the user
# until a blank line is entered. Once all of the integers have been read, your program
# should display all of the negative numbers, followed by all of the zeros, followed by all
# of the positive numbers. Within each group the numbers should be displayed in the
# same order that they were entered by the user. For example, if the user enters the values
# 3, -4, 1, 0, -1, 0, and -2 then your program should output the values -4, -1, -2, 0, 0, 3,
# and 1. Your program should display each value on its own line.
# Hint: You can use seprate lists to store the values as they are coming in from the
# user.

def reading_list():
    while True:
        no=input("number to be entered: ")
        if no !="":
            no=int(no)
            if no<0:
                no_list_neg.append(no)
            elif no>0:
                no_list_positive.append(no)
            else:
                no_zero.append(no)
            
        else:
            break



def main():
    global no_list_neg, no_list_positive, no_zero
    no_list_neg = []
    no_list_positive = []
    no_zero = []
    reading_list()
    print(no_list_neg+no_zero+no_list_positive)

if __name__ == "__main__":
    main()