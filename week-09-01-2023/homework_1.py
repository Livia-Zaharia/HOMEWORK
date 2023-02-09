#1.name and address for mailing
print("+"*25)
print("ex.1")
print("+"*25)
print('\n'*3)

first_name="Livia"
last_name="Zaharia"
mailing_address="Cal.Grivitei, nr 160, Bl B, Apt 12"
city="BUCHAREST"
country="ROMANIA"

print("SENDER: "+first_name+" "+last_name)
print("ADDRESS: "+mailing_address)
print("CITY: "+city)
print("COUNTRY: "+country)

#2.WIDTH AND LENGHT OF ROOM  (FLOAT)=>AREA
print('\n'*5)
print("---"*25)
print("+"*25)
print("ex.2")
print("+"*25)
print('\n'*3)

room_width=float(input("Room width (m): "))
room_length=float(input("Room length (m): "))
room_area= room_length * room_width

print("Room area="+str(room_area)+" square meters")

#3.recycling
print('\n'*5)
print("---"*25)
print("+"*25)
print("ex.3")
print("+"*25)
print('\n'*3)

print("large containers= 1 l or more--->$0.25")
print("small containers= less than 1 l--->$0.10")

large_container=int(input("No of large containers= "))
small_container=int(input("No of small containers= "))

print("Total discount --->$"+str(large_container*0.25 + small_container*0.1))


#4.tip
print('\n'*5)
print("---"*25)
print("+"*25)
print("ex.4")
print("+"*25)
print('\n'*3)

meal_price=float(input("The bill to pay for the meal is "))
meal_price=round(meal_price,2)
print("GRAND TOTAL")
print("---"*5)
print(round(meal_price*1.1,2))
print("---"*5)
print("MEAL--->"+str(round(meal_price-round(meal_price*0.2,2),2)))
print("VAT--->"+str(round(meal_price*0.2,2)))
print("TIP--->"+str(round(round(meal_price*1.1,2)-meal_price,2)))

#5.sum of first n numbers
print('\n'*5)
print("---"*25)
print("+"*25)
print("ex.5")
print("+"*25)
print('\n'*3)

number_limit=int(input("Counting to..."))
print ("and their sum is "+str(((number_limit+1) * number_limit)/2))

#6.
print('\n'*5)
print("---"*25)
print("+"*25)
print("ex.6")
print("+"*25)
print('\n'*3)

a=int(input("a= "))
b=int(input("b= "))

print("a+b="+str(a+b))
print("b-a="+str(b-a))
print("a*b="+str(a*b))
print("a//b="+str(a//b))
print("a%b="+str(a%b))
print("pow(a,b)="+str(pow(a,b)))

#7.feet and inches
print('\n'*5)
print("---"*25)
print("+"*25)
print("ex.7")
print("+"*25)
print('\n'*3)

height_feet=int(input("you height in feet...."))
height_inches=int(input("...and inches...."))

print ("your height in cm..."+str((12*height_feet+height_inches)*2.54))

#8.area of circle and volume of sphere
print('\n'*5)
print("---"*25)
print("+"*25)
print("ex.8")
print("+"*25)
print('\n'*3)

import math

radius=float(input("radius is...."))
print("area is "+ str(math.pi*pow(radius,2)))
print("volume is "+ str(math.pi*pow(radius,3)*4/3))