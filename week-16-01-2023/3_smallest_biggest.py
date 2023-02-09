# 3. Smallest and Biggest: Write a program that reads a sequence of integers 
# from the user and displays at the end the biggest and the smallest number 
# that they have introduced.

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
    

print("The max value is="+str(max(number_list)))
print("The min value is="+str(min(number_list)))
    