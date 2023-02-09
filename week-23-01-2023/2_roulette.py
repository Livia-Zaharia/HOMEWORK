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
#any further output

def roulette_color():
    colors=[]
    for i in range(0,38):
        if i==0:
            colors.append(0)
        elif i==37:
            colors.append(0)
        elif i<=18:
            if (i%2==1 and i<=9) or (i%2==0 and i>9):
                colors.append(2)
            else:
                colors.append(1)
        else:
            if (i%2==1 and i<=27) or (i%2==0 and i>27):
                colors.append(2)
            else:
                colors.append(1)
    

    return colors



import random
r_c=roulette_color()

roulette=random.randint(0,37)
print ("The spin resulted in "+str(roulette)+"....")
if roulette==0:
    print("Pay 0")
elif roulette==37:
    print("Pay 00")
else:
    print("Pay "+ str(roulette))
    if (r_c[roulette]==1):
        print("Pay Black")
    else:
        print("Pay Red")


    if(roulette%2!=0):
        print ("Pay Odd")
    else:
        print("Pay Even")



    if(roulette<=18):
        print ("Pay 1 to 18")
    else:
        print("Pay 19 to 36")