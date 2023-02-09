
def running_in_list(g_l:list):
    for element in g_l:
        
        if (type(element)!= list):
            check_type(element)
        elif ((type(element)== list)):
            running_in_list(element)

def check_type(x):
    
    if type(x)== str:
        global letter
        letter=letter+x
    elif type(x)== int:
        global sum
        sum=sum+x


general_list=[1,5,8,["a",7,10,[13,"b"],"c",[["d"],11],12,["e"]],"f",18]
letter="+"
sum=0
# print (type(general_list)== list)
# for elem in general_list:
    # print(elem)

running_in_list(general_list)
letter=letter.strip("+")
print(letter)
print(sum)