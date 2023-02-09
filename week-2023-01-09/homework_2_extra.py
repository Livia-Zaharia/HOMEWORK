#1. Dog Years: It is commonly said that one human year is equivalent to 7 dog years. However
#this simple conversion fails to recognize that dogs reach adulthood in approximately two
#years. As a result, some people believe that it is better to count each of the first two human
#years as 10.5 dog years, and then count each additional human year as 4 dog years. Write a
#program that implements the conversion from human years to dog years described in the
#previous paragraph. Ensure that your program works correctly for conversions of less than
#two human years and for conversions of two or more human years. Your program should
#display an appropriate error message if the user enters a negative number.


print("+"*25)
print("ex.1")
print("+"*25)
print('\n'*3)

human_time=float(input("Age of dog in human years "))

if human_time<0:
    print("Can't have negative values")
elif human_time-2<0:
    dog_age=10.5*human_time
    print("Dog years as follows "+str(dog_age))
elif human_time-2>=0:
    dog_age=(10.5*2)+4*(human_time-2)
    print("Dog years as follows "+str(dog_age))


#2. Sound Levels: The following table lists the sound level in decibels for several common
#noises.
#Write a program that reads a sound level in decibels from the user. If the user enters a decibel
#level that matches one of the noises in the table then your program should display a message
#containing only that noise. If the user enters a number of decibels between the noises listed then
#your program should display a message indicating which noises the level is between. Ensure that
#your program also generates reasonable output for a value smaller than the quietest noise in the
#table, and for a value larger than the loudest noise in the table.

print("+"*25)
print("ex.2")
print("+"*25)
print('\n'*3)

sound=float(input("The value of sound to be checked "))
if sound<40:
    print("this value is quieter than a quiet room")
elif sound==40:
    print("this value is as quiet as quiet room")
elif sound>40 and sound<70:
    print("this value is somewhere between a quiet room and an alarm clock")
elif sound==70:
    print("this value is as noisy as an alarm clock")
elif sound>70 and sound<103:
    print("this value is somewhere in between an alarm clock and a gas lawnmower")
elif sound==103:
    print("this value is as loud as a gas lawnmower")
elif sound>103 and sound<130:
    print("this value is somewhere in between a gas lawnmower and a jackhammer")
elif sound==130:
    print("this value is as loud as jackhammer")
else:
    print("this value is louder than a jackhammer")



#3. What Color is that Square?: Positions on a chess board are identified by a letter and a
#number. The letter identifies the column, while the number identifies the row, as shown
#below:
#Write a program that reads a position from the user. Use an if statement to determine if the
#column begins with a black square or a white square. Then use modular arithmetic to report the
#color of the square in that row. For example, if the user enters a1 then your program should
#report that the square is black. If the user enters d5 then your program should report that the
#square is white. Your program may assume that a valid position will always be entered. It does
#not need to perform any error checking.

print("+"*25)
print("ex.3")
print("+"*25)
print('\n'*3)
letters =["0","a","b","c","d","e","f","g","h"]
position=input("Square to be analyzed ")


if letters.index(position[0])%2 ==0:
    if int(position[1])%2 ==0:
        print("First square of this column is white")
        print ("and this square in particular is black")
    else:
        print("First square of this column is white")
        print ("and this square in particular is white")
else:
    if int(position[1])%2 ==0:
        print("First square of this column is black")
        print ("and this square in particular is white")
    else:
        print("First square of this column is black")
        print ("and this square in particular is black")
    


#4. Chinese Zodiac: The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year
#cycle is shown in the table below. The pattern repeats from there, with 2012 being another
#year of the dragon, and 1999 being another year of the hare.
#Write a program that reads a year from the user and displays the animal associated with that
#year. Your program should work correctly for any year greater than or equal to zero, not just the
#ones listed in the table.

print("+"*25)
print("ex.4")
print("+"*25)
print('\n'*3)

years=["monkey", "rooster", "dog","pig", "rat", "ox","tiger", "hare", "dragon", "snake", "horse", "sheep"]

date=int(input("What is your year? "))
print("That is the year of the "+years[date%12])


#5. Letter Grade to Grade Points: At a particular university, letter grades are mapped to grade
#points in the following manner:
#Write a program that begins by reading a letter grade from the user. Then your program should
#compute and display the equivalent number of grade points. Ensure that your program generates
#an appropriate error message if the user enters an invalid letter grade.

print("+"*25)
print("ex.5")
print("+"*25)
print('\n'*3)

grades_letters=["F","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
grades_number=[0.0,1.0,1.3,1.7,2.0,2.3,2.7,3.0,3.3,3.7,4.0,4.0]

letter_grade=input("what grade did they give you? ")

try:
    print("that means "+ str(grades_number[grades_letters.index(letter_grade)])+" in points")
except ValueError:
    print("that grade doesn't exist")



#6. Grade Points to Letter Grade: In the previous exercise you created a program that converts
#a letter grade into the equivalent number of grade points. In this exercise you will create a
#program that reverses the process and converts from a grade point value entered by the
#user to a letter grade. Ensure that your program handles grade point values that fall between
#letter grades. These should be rounded to the closest letter grade. Your program should
#report A+ for a 4.0 (or greater) grade point average.


print("+"*25)
print("ex.6")
print("+"*25)
print('\n'*3)

grades_letters=["F","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
grades_number=[0.0,1.0,1.3,1.7,2.0,2.3,2.7,3.0,3.3,3.7,4.0,4.0]

grade=float(input("what grade did they give you? "))

no_min=0

no_max=len(grades_number)-1

no_mid=(len(grades_number)//2)

check =0

if grade>=4.0:
    print ("Your grade in A+")
else:
    while no_mid-no_min >=1:
        if grade==grades_number[no_mid]:
            print("your grade is "+ grades_letters[no_mid])
            check=1
            break
        elif grade<grades_number[no_mid]:
            no_max=no_mid
            no_mid=(no_mid-no_min)//2+no_min
            print("moving to the left")
            print(no_min)
            print(grades_number[no_min])
            print("++++")
            print(no_mid)
            print(grades_number[no_mid])
            print("++++")
            print(no_max)
            print(grades_number[no_max])
        elif grade>grades_number[no_mid]:
            no_min=no_mid
            no_mid=(no_max-no_mid)//2+no_min
            print("moving to the right")
            print(no_min)
            print(grades_number[no_min])
            print("++++")
            print(no_mid)
            print(grades_number[no_mid])
            print("++++")
            print(no_max)
            print(grades_number[no_max])
            
    if check==0:
        print("Your grade is between "+str(grades_letters[no_min])+" and "+str(grades_letters[no_max]))




#7. Cell Phone Bill: A particular cell phone plan includes 50 minutes of air time and 50 text
#messages for $15.00 a month. Each additional minute of air time costs $0.25, while
#additional text messages cost $0.15 each. All cell phone bills include an additional charge of
#$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is subject to 5
#percent sales tax. Write a program that reads the number of minutes and text messages
#used in a month from the user. Display the base charge, additional minutes charge (if any),
#additional text message charge (if any), the 911 fee, tax and total bill amount. Only display
#the additional minute and text message charges if the user incurred costs in these
#categories. Ensure that all of the charges are displayed using 2 decimal places.


print("+"*25)
print("ex.7")
print("+"*25)
print('\n'*3)

minutes_month=int(input("minutes/month= "))
text_mess=int(input("Messages/month= "))
if minutes_month-50>0 and text_mess-50>0:
    additional_minutes=(minutes_month-50)*0.25
    additional_text=(text_mess-50)*0.15
    cost=15.00+(minutes_month-50)*0.25+(text_mess-50)*0.15+0.44
else:
    cost=15.00+0.44
    additional_text=0
    additional_minutes=0
print("BASE CHARGE= $15.00")
print("Extra minutes charge= $"+"{:.2f}".format(additional_minutes))
print("Extra text charge= $"+"{:.2f}".format(additional_text))
print("911 extra charge= $0.44")
print("Sales tax 5%= "+"{:.2f}".format(cost*0.05))
print("TOTAL----"+"{:.2f}".format(cost*1.05))




#8. Roulette Payouts: A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are
#red, and two are green. The green spaces are numbered 0 and 00. The red spaces are
#numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining
#integers between 1 and 36 are used to number the black spaces. Many different bets can be
#placed in roulette. We will only consider the following subset of them in this exercise:
#1. Single number (1 to 36, 0, or 00)
#2. Red versus Black
#3. Odd versus Even (Note that 0 and 00 do not pay out for even)
#4. 1 to 18 versus 19 to 36
#Write a program that simulates a spin of a roulette wheel by using Python’s random number
#generator or read it from the user. Display the number that was selected and all of the bets
#that must be payed. For example, if 13 is selected then your program should display:
#The spin resulted in 13...
#Pay 13
#Pay Black
#Pay Odd
#Pay 1 to 18
#If the simulation results in 0 or 00 then your program should display Pay 0 or Pay 00 without
#any further outp

print("+"*25)
print("ex.8")
print("+"*25)
print('\n'*3)

import random

roulette=random.randint(0,37)
print ("The spin resulted in "+str(roulette)+"....")
if roulette==0:
    print("Pay 0")
elif roulette==37:
    print("Pay 00")
elif roulette<=18:
    print("Pay "+ str(roulette))
    if (roulette%2==1 and roulette<=9) or (roulette%2==0 and roulette>9):
        print("Pay Black")
    else:
        print("Pay white")
    if(roulette%2==0):
        print ("Pay Odd")
    else:
        print("Pay Even")
    
    print ("Pay 1 to 18")
else:
    print("Pay "+ str(roulette))
    if (roulette%2==1 and roulette<=27) or (roulette%2==0 and roulette>27):
        print("Pay Black")
    else:
        print("Pay white")
    if(roulette%2==0):
        print ("Pay Odd")
    else:
        print("Pay Even")
    print("Pay 19 to 36")