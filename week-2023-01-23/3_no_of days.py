#4. The length of a month varies from 28 to 31 days. In this exercise you will create a program
#that reads the name of a month from the user as a string. Then your program should display
#the number of days in that month. Display “28 or 29 days” for February so that leap years are
#addressed.
def year_type(year):
    if year%400 == 0:
        return 1
    elif year%100 == 0:
        return 0
    elif year%4 == 0:
        return 1
    else:
        return 0

#year_type returns 1 if leap year, else 0

days_months=[0,31,1,31,30,31,30,31,31,30,31,30,31]
months_name=["0","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
search_month=input("What month do you want to know the number of days of? ")
search_year= int(input("And what year is that? "))


try:
    if months_name.index(search_month.upper()) > 0 and months_name.index(search_month.upper()) <= 12 and months_name.index(search_month.upper()) != 2:
        print("That month has ", end="")
        print(days_months[months_name.index(search_month.upper())],end="")
        print(" days")
    elif months_name.index(search_month.upper()) == 2 :
        if year_type(search_year)==1:
            print("That month has 29 days")
        else:
            print("That month has 28 days")
except ValueError:
    print("there is no such month")

