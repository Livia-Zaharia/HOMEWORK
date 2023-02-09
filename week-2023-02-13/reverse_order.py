
# 2. Reverse Order1
# : Write a program that reads integers from the user and stores them in a
# list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have
# been read your program should display them (except for the 0) in reverse order, with
# one value appearing on each line.
# Hint: Don't forget that most of the list methods are acting in place, changing the list
# itself.

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
    no_list.reverse()
    for elem in no_list:
        print(elem)

if __name__ == "__main__":
    main()