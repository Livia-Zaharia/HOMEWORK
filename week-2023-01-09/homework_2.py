# #1. Write a program that reads an integer from the user. Then your program should display a
# #message indicating whether the integer is even or odd
# print("+"*25)
# print("ex.1")
# print("+"*25)
# print('\n'*3)

# number=int(input("Number to be checked if odd or even "))
# if number%2 ==0 :
#     print("Number was even")
# else:
#     print("Number was odd")


# #2. In this exercise you will create a program that reads a letter of the alphabet from the user. If
# #the user enters a, e, i, o or u then your program should display a message indicating that the
# #entered letter is a vowel. If the user enters y then your program should display a message
# #indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your
# #program should display a message indicating that the letter is a consonant.

# print("+"*25)
# print("ex.2")
# print("+"*25)
# print('\n'*3)

# letter=input("Present a letter ")
# if letter.upper() == "A" or letter.upper() == "E" or letter.upper() == "I" or letter.upper() == "O" or letter.upper() == "U":
#     print("Letter is a vowel")
# elif letter.upper() == "Y":
#     print("This letter might be a vowel or a consonant depending on other letters")
# else:
#     print("Letter is a consonant")


# #3. Write a program that determines the name of a shape from its number of sides. Read the
# #number of sides from the user and then report the appropriate name as part of a
# #meaningful message. Your program should support shapes with anywhere from 3 up to (and
# #including) 10 sides. If a number of sides outside of this range is entered then your program
# #should display an appropriate error message.

# print("+"*25)
# print("ex.3")
# print("+"*25)
# print('\n'*3)

# shapes =["0","1","2","triangle","square","pentagon","hexagon","heptagon","octagon","nonagon","decagon"]
# nr_sides=int(input("Number of sides of polygon "))
# if nr_sides >= len(shapes):
#     print("Error.Too many sides to count")
# elif nr_sides < 3:
#     print("Error. Can't be a closed polygon")
# else:
#     print("what you entered is a "+shapes[nr_sides])

#4. The length of a month varies from 28 to 31 days. In this exercise you will create a program
#that reads the name of a month from the user as a string. Then your program should display
#the number of days in that month. Display “28 or 29 days” for February so that leap years are
#addressed.

# print("+"*25)
# print("ex.4")
# print("+"*25)
# print('\n'*3)

# days_months=[0,31,1,31,30,31,30,31,31,30,31,30,31]
# months_name=["0","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
# search_month=input("What month do you want to know the number of days of? ")

# try:
#     if months_name.index(search_month.upper()) > 0 and months_name.index(search_month.upper()) <= 12 and months_name.index(search_month.upper()) != 2:
#         print("That month has ", end="")
#         print(days_months[months_name.index(search_month.upper())],end="")
#         print(" days")
#     elif months_name.index(search_month.upper()) == 2 :
#         print("That month might have 29 or 28 days")
# except ValueError:
#     print("there is no such month")


#5. A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
#scalene. All 3 sides of an equilateral triangle have the same length. An isosceles triangle has
#two sides that are the same length, and a third side that is a different length. If all of the
#sides have different lengths then the triangle is scalene. Write a program that reads the
#lengths of 3 sides of a triangle from the user. Display a message indicating the type of the
#triangle.

print("+"*25)
print("ex.5")
print("+"*25)
print('\n'*3)  

side_1=int(input("First side of triangle has "))
side_2=int(input("Second side of triangle has "))
side_3=int(input("Third side of triangle has "))

if side_1 > side_2:
    side_1, side_2 = side_2, side_1
if side_2 > side_3:
    side_2, side_3= side_3, side_2
if side_2 < side_1:
    side_2, side_1= side_1, side_2

#print(side_1)
#print(side_2)
#print(side_3)


if side_1 == side_2 and side_2 == side_3:
    print("triangle is equilateral")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print ("triangle is isosceles")
else:
    print ("triangle is scalene")

if pow(side_3,2) == pow(side_1,2)+pow(side_2,2):
    print("....and is a right angle one")

#7. The year is divided into four seasons: spring, summer, fall and winter. While the exact dates
#that the seasons change vary a little bit from year to year because of the way that the
#calendar is constructed, we will use the following dates for this exercise
#0320-spring
#0621- summer
#0922- autumn
#1221- winter
#Create a program that reads a month and day from the user. The user will enter the name of the
#month as a string, followed by the day within the month as an integer. Then your program should
#display the season associated with the date that was entered.

print("+"*25)
print("ex.7")
print("+"*25)
print('\n'*3)

days_months=[0,31,29,31,30,31,30,31,31,30,31,30,31]
months_name=["0","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
search_month=input("What month are you in? ")
search_day=int(input("And what day? "))

try:
    search_month=months_name.index(search_month.upper())
    if search_month > 0 and search_month <= 12 and search_day<=days_months[search_month] and search_day!=0 :
        search_input=search_month*100 + search_day
        if (search_input >= 1224 and search_input <= 1231) or (search_input<320):
            print ("This is WINTER")
        elif search_input >= 320 and search_input < 621:
            print("This is SPRING")
        elif search_input >= 621 and search_input < 922:
            print("This is SUMMER")
        else:
            print ("This is AUTUMN")
    else:
        print("There is no such day")
except ValueError:
    print("there is no such month")


#9. At a particular company, employees are rated at the end of each year. The rating scale
#begins at 0.0, with higher values indicating better performance and resulting in larger raises.
#The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values between 0.0 and
#0.4, and between 0.4 and 0.6 are never used. The meaning associated with each rating is
#shown in the following table. The amount of an employee’s raise is $2400.00 multiplied by
#their rating.
#Write a program that reads a rating from the user and indicates whether the performance was
#unacceptable, acceptable or meritorious. The amount of the employee’s raise should also be
#reported. Your program should display an appropriate error message if an invalid rating is
#entered.

print("+"*25)
print("ex.9")
print("+"*25)
print('\n'*3)  

rating_value=float(input("Please provide the rating for your employee "))

if rating_value >= 0.6:
    print("The employee's performance was meritorious")
    print("Raise amount is $"+str(rating_value*2400))
elif rating_value == 0.4:
    print("The employee's performance was acceptable")
    print("Raise amount is $"+str(rating_value*2400))
elif rating_value == 0:
    print("The employee's performance was unacceptable")
else:
    print("There is no such rating")


#10. Most years have 365 days. However, the time required for the Earth to orbit the Sun is
#actually slightly more than that. As a result, an extra day, February 29, is included in some
#years to correct for this difference. Such years are referred to as leap years. The rules for
#determining whether or not a year is a leap year follow:
#Any year that is divisible by 400 is a leap year,
#Of the remaining years, any year that is divisible by 100 is not a leap year,
#Of the remaining years, any year that is divisible by 4 is a leap year.
#All other years are not leap years.
#Write a program that reads a year from the user and displays a message indicating
#whether or not it is a leap year.


print("+"*25)
print("ex.10")
print("+"*25)
print('\n'*3)

year=int(input("What year are you going to check? "))


if year%400 == 0:
    print("Leap year since it divides by 400")
elif year%100 == 0:
    print("Not leap year because it divides by 100 but not 400")
elif year%4 == 0:
    print ("Leap year because even though it doesn't divide by 400 but it does divide by 4")
else:
    print ("not leap year")
