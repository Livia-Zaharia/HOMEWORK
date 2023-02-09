
# 4. Buy 8 Get 1 Free2
# Write a program that has a inputs named number_of_coffees and price_per_coffee
# Given this information, the program displays the total cost of the coffee
# order. This is not a simple multiplication of cost and quantity, however,
# because the coffee shop has an offer where you get one free coffee for every 
# eight coffees you buy. For example, buying eight coffees for $2.50 each costs $20
# (or 8 × 2.5). But buying nine coffees also costs $20, since the first eight makes
# the ninth coffee free. Buying ten coffees calculates as follows: $20 for the 
# first eight coffees, a free ninth coffee, and $2.50 for the tenth coffee
# for a total of $22.50.

no_coffees=int(input("How many coffees? "))
price_coffee=float(input("And at what price?" ))

if(no_coffees<=8):
    print("For "+ str(no_coffees)+" the price is "+ str(no_coffees*price_coffee)+"$")
else:
    print("For "+ str(no_coffees)+" the price is "+ str(8*(no_coffees//8)*price_coffee + (no_coffees%8)*price_coffee - (no_coffees//8)*price_coffee)+"$")
