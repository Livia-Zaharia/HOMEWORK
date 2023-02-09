# 3. Smallest and Biggest: Write a program that reads a sequence of integers 
# from the user and displays at the end the biggest and the smallest number 
# that they have introduced.

def order_num(number:int) ->str:
    sufix=["th","st","nd","rd"]
    check=number%10
    if check>=4:
        check=0

    if number==11:
        return("11th")
    elif number==12:
        return("12th")
    elif number==13:
        return("13th")
    else:
        return(str(number)+sufix[check])


switch=1
number_list=[]
while True:
    to_be_added=input("number ")

    if to_be_added != "" and to_be_added[0]=="-" :
        to_be_added=to_be_added.strip("-")
        switch=-1

        
    if(to_be_added.isdecimal()):
        #is decimal nu merge pe negativ!!!!
        number_list.append(int(to_be_added)*switch)
        switch=1
    elif (to_be_added == ""):
        break
    else:
        pass
    

print("The max value is="+str(max(number_list))+" and is the "+order_num(number_list.index(max(number_list))+1)+" entered")
print("The min value is="+str(min(number_list))+" and is the "+order_num(number_list.index(min(number_list))+1)+" entered")


