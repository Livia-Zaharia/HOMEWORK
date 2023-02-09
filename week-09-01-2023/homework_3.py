#1. Average: In this exercise you will create a program that computes the average of a collection
#of values entered by the user. The user will enter 0 as a sentinel value to indicate that no
#further values will be provided. Your program should display an appropriate error message if
#the first value entered by the user is 0.
#Hint: Read the values in a loop and sum all the values in a variable and keep another
#variable as the counter. Because the 0 marks the end of the input it should not be
#included in the average.

print("+"*25)
print("ex.1")
print("+"*25)
print('\n'*3)

number=1
count=0
sum=0
while number!=0:
    number=int(input("number to be added"))
    if number==0:
        if count==0:
            print("The series should have more than one item which differs from 0")
            break
        else:
            break
    sum=sum+number
    count+=1
if count!=0:
    print("the average fo this series is "+str(sum/count))

#2. Temperature Conversion Table: Write a program that displays a temperature conversion
#table for degrees Celsius and degrees Fahrenheit. The table should include rows for all
#temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
#Include appropriate headings on your columns. The formula for converting between degrees
#Celsius and degrees Fahrenheit can be found on the internet.


print("+"*25)
print("ex.2")
print("+"*25)
print('\n'*3)
print("Celsius...Farenheit")
for i in range(0,100,10):
    if i==0:
        print(str(i)+".."+"..."*3+str(i*(9/5)+32))
    elif i==100:
        print(str(i)+"..."*3+str(i*(9/5)+32))
    else:
        print(str(i)+"."+"..."*3+str(i*(9/5)+32))




#3. Compute the Perimeter of a Polygon: Write a program that computes the perimeter of a
#polygon. Begin by reading the number of sides and then read the length of each side using a
#loop. Display the perimeter at the end.


print("+"*25)
print("ex.3")
print("+"*25)
print('\n'*3)

number=1
count=0
sum=0
sides=int(input("number of sides to be added "))
if sides<3:
    print("you have to have at least 3 sides to any polygon")
else:
    while count<sides:
        number=int(input("length of side to add "))
        sum=sum+number
        count+=1
    print("the perimeter for this polygon is "+str(sum))


#4. Admission Price: A particular zoo determines the price of admission based on the age of the
#guest. Guests 2 years of age and less are admitted without charge. Children between 3 and
#12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission for all
#other guests is $23.00. Create a program that begins by reading the ages of all of the guests
#in a group from the user, with one age entered on each line. The user will enter a blank line
#to indicate that there are no more guests in the group. Then your program should display
#the admission cost for the group with an appropriate message. The cost should be displayed
#using two decimal places.

print("+"*25)
print("ex.4")
print("+"*25)
print('\n'*3)
price=0

guest= input("age of guest ")
while guest !="":
    if int(guest)<=2:
        price=price+0
    elif int(guest)>2 and int(guest)<=12:
        price+=14.00
    elif int(guest)>=65:
        price+=18.00
    else:
        price+=23.00
    guest= input("age of guest ")
print("total price for everyone is "+ "{:.2f}".format(price))



#5. Approximate π: The value of π can be approximated by the following infinite series:
#Write a program that displays 15 approximations of π. The first approximation should make
#use of only the first term from the infinite series. Each additional approximation displayed by
#your program should include one more term in the series, making it a better approximation
#of π than any of the approximations displayed previously.


print("+"*25)
print("ex.5")
print("+"*25)
print('\n'*3)
aprox_pi=3

no=int(input("number of iterations "))
for i in range(1,no+1):
    print("aproximation no "+str(i)+":"+str(aprox_pi))
    aprox_pi=(2*(i%2)-1)*(1/(i*(2*i+1)*(i+1)))+aprox_pi



#6. Multiplication Table: In this exercise you will create a program that displays a multiplication
#table that shows the products of all combinations of integers from 1 times 1 up to and
#including 10 times 10. Your multiplication table should include a row of labels across the top
#of it containing the numbers 1 through 10. It should also include labels down the left side
#consisting of the numbers 1 through 10. The expected output from the program is shown
#below:
#When completing this exercise you will probably find it helpful to be able to print out a value
#without moving down to the next line. This can be accomplished by added end="" as the
#last parameter to your print statement. For example, print("A") will display the letter A
#and then move down to the next line. The statement print("A", end="") will display the
#letter A without moving down to the next line, causing the next print statement to display its
#result on the same line as the letter A.



print("+"*25)
print("ex.6")
print("+"*25)
print('\n'*3)

print ("    ", end="")
for i in range (1,11):
    print ("{:>2}".format(str(i))+" ", end="")
print('\n')

for i in range(1,11):
    print("{:>2}".format(str(i))+"  ", end="")
    for j in range (1,11):
        print ("{:>2}".format(str(j*i))+" ", end="")
    print (' ')


#7. Greatest Common Divisor: The greatest common divisor of two positive integers, n and m,
#is the largest number, d, which divides evenly into both n and m. There are several
#algorithms that can be used to solve this problem, including:
#Write a program that reads two positive integers from the user and uses this algorithm to
#determine and report their greatest common divisor.


print("+"*25)
print("ex.7")
print("+"*25)
print('\n'*3)

no_1=int(input("specify first number: "))
no_2=int(input("specify second number: "))

if no_1<no_2:
    d=no_1
else:
    d=no_2
while no_1%d !=0 or no_2%d !=0:
    d=d-1
if d!=0:
    print("greatest common divisior is "+str(d))


#8. Prime Factors: The prime factorization of an integer, n, can be determined using the
#following steps:
#Write a program that reads an integer from the user. If the value entered by the user is less
#than 2 then your program should display an appropriate error message. Otherwise your
#program should display the prime numbers that can be multiplied together to compute n,
#with one factor appearing on each line. For example:



print("+"*25)
print("ex.8")
print("+"*25)
print('\n'*3)

f=2
no_3=int(input("Number to be deconstructed into prime numbers: "))
print("Prime factors:")

while f<=no_3:
    if no_3%f == 0:
        print(f)
        no_3=no_3//f
    else:
        f=f+1

#9. Maximum Integer:Create a program that begins by selecting a random integer between 1 and 100. Save this integer as the
#maximum number encountered so far. After the initial integer has been selected, generate
#99 additional random integers between 1 and 100. Check each integer as it is generated to
#see if it is larger than the maximum number encountered so far. If it is then your program
#should update the maximum number encountered and count the fact that you performed
#an update. Display each integer after you generate it. Include a notation with those integers
#which represent a new maximum.
#After you have displayed 100 integers your program should display the maximum value
#encountered, along with the number of times the maximum value was updated during the
#process. Partial output for the program is shown below, with … representing the remaining
#integers that your program will display. Run your program several times. Is the number of
#updates performed on the maximum value what you expected?

print("+"*25)
print("ex.9")
print("+"*25)
print('\n'*3)

import random

count=1
updates=0

max=random.randint(1,100)
print(max)
while count<101:
    temp=random.randint(1,100)
    if(max<temp):
        max=temp
        print(str(max)+"<==Update")
        updates+=1
    else:
        print(temp)
    count=count+1
print("the maximum value found was "+str(max))
print("the were "+str(updates)+" updates")