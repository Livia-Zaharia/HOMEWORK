# 1. Sorted Order1
# : Write a program that reads integers from the user and stores them in a
# list. Your program should continue reading values until the user enters 0. Then it should
# display all of the values entered by the user (except for the 0) in order from smallest to
# largest, with one value appearing on each line. Use the sort method to sort the list.
# Hint: We can read values forever using a loop, just like we have done in the past
# lessons.




def reading_list():
    while True:
        no=int(input("number to be entered: "))
        if no !=0:
            no_list.append(no)
        else:
            break



def main():
    global no_list
    no_list = []
    reading_list()
    no_list.sort()
    print(no_list)

if __name__ == "__main__":
    main()