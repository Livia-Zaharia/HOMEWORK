# 2. Ordinal Suffix2
# Write an ordinal suffix program with an integer input named number and output a 
# string of the number with its ordinal suffix.

sufix=["th","st","nd","rd"]
number=int(input("date to be converted into ordinal numeral "))
check=number%10
if check>=4:
    check=0
    
if number==11:
    print("11th")
elif number==12:
    print("12th")
elif number==13:
    print("13th")
else:
    print(str(number)+sufix[check])