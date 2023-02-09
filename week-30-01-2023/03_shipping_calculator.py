
# 3. Shipping Calculator1
# : An online retailer provides express shipping for many of its items at a
# rate of $10.95 for the first item, and $2.95 for each subsequent item. Write a function that
# takes the number of items in the order as its only parameter. Return the shipping charge for
# the order as the function’s result.


def shippment_cost(no_items:int) ->float:
    cost=base_rate+(no-1)*item_fare
    return cost

base_rate=10.95
item_fare=2.95

no=int(input("how many items would you like to send? "))
print("total cost ",shippment_cost(no)," $")