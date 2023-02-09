
# 4. Median of Three Values1
# : Write a function that takes three numbers as parameters, and
# returns the median value of those parameters as its result.
# Hint: The median value is the middle of the three values when they are sorted into
# ascending order. It can be found using if statements, or with a little bit of mathematical
# creativity.

def median(no_list:list, count:int) ->float:
    if count%2!=0:
        return no_list[count//2]
    else:
        return (no_list[count//2]+no_list[(count//2)-1])/2

def sort_list(no_list:list) ->list:
    rebuilt=[]
    while no_list:
        rebuilt.append(min(no_list))
        no_list. remove(min(no_list))
    
    return rebuilt



no_list=[]
count=0
while True:
    no=input("number: ")
    if no!="":
        no=float(no)
        no_list.append(no)
        count+=1
    else:
        break
print (no_list)
sorted=sort_list(no_list)
print (sorted)
print("Median is ",median(sorted,count))