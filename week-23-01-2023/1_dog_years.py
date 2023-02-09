#1. Dog Years: It is commonly said that one human year is equivalent to 7 dog years. However
#this simple conversion fails to recognize that dogs reach adulthood in approximately two
#years. As a result, some people believe that it is better to count each of the first two human
#years as 10.5 dog years, and then count each additional human year as 4 dog years. Write a
#program that implements the conversion from human years to dog years described in the
#previous paragraph. Ensure that your program works correctly for conversions of less than
#two human years and for conversions of two or more human years. Your program should
#display an appropriate error message if the user enters a negative number.
def dividend(no:float) ->int:
    no*=100
    no=int(no)
    return no//100

def reminder(no:float) ->int:
    no*=100
    no=int(no)
    return no%100

def aprox_percent(percent,value):
    return percent*value


human_time=float(input("Age of dog in human years "))

if human_time<0:
    print("Can't have negative values")
elif human_time-2<0:
    dog_age=10.5*human_time
    print("Dog years as follows "+str(dog_age))
    
    dog_age_years=dividend(dog_age)
    dog_age_months=reminder(dog_age)
    
    dog_age_months=aprox_percent(float(dog_age_months)/100,12)

    if dog_age_months!=0:
        dog_age_days=reminder(dog_age_months)
        dog_age_days=round(aprox_percent(float(dog_age_days)/100,30))
        dog_age_months=dividend(dog_age_months)
    else:
        dog_age_days=0
    
    print("Or, more precise "+str(dog_age_years)+" years, "+str(dog_age_months)+" months and "+str(dog_age_days)+" days")

    

elif human_time-2>=0:
    dog_age=(10.5*2)+4*(human_time-2)
    print("Dog years as follows "+str(dog_age))

    dog_age_years=dividend(dog_age)
    dog_age_months=reminder(dog_age)
    
    dog_age_months=aprox_percent(float(dog_age_months)/100,12)

    if dog_age_months!=0:
        dog_age_days=reminder(dog_age_months)
        dog_age_days=round(aprox_percent(float(dog_age_days)/100,30))
        dog_age_months=dividend(dog_age_months)
    else:
        dog_age_days=0
    
    print("Or, more precise "+str(dog_age_years)+" years, "+str(dog_age_months)+" months and "+str(dog_age_days)+" days")
