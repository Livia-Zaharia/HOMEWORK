
# 2. Taxi Fare1
# : In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for
# every 140 meters traveled. Write a function that takes the distance traveled (in kilometers) as
# its only parameter and returns the total fare as its only result.
# Hint: Taxi fares change over time. Use constants to represent the base fare and the
# variable portion of the fare so that the program can be updated easily when the rates
# increase.

def taxi_fare(dist:float) ->float:
    cost=base_fare+dist_fare*dist*1000/140
    return cost

base_fare=4
dist_fare=0.25

dist=float(input("how many km have you traveled? "))
print("total cost is ",taxi_fare(dist),"$")