""""

 Write Out Numbers in English2
: While the popularity of cheques as a payment method has
diminished in recent years, some companies still issue them to pay employees or vendors.
The amount being paid normally appears on a cheque twice, with one occurrence written
using digits, and the other occurrence written using English words. Repeating the amount in
two different forms makes it much more difficult for an unscrupulous employee or vendor to
modify the amount on the cheque before depositing it. In this exercise, your task is to create
a function that takes an integer between 0 and 999 as its only parameter, and returns a
string containing the English words for that number. For example, if the parameter to the
function is 142 then your function should return “one hundred forty two”. Use one or more
dictionaries to implement your solution rather than large if/elif/else constructs. Include a
main program that reads an integer from the user and displays its value in English words.

"""

def write_no(no_i:int):
    simple_dict={
        1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
        7:"seven", 8:"eight", 9:"nine", 10:"ten", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
        70:"seventy", 80:"eighty", 90:"ninety", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen",
        17:"seventeen", 18:"eighteen", 19:"nineteen"
    }

    if len(str(no_i))==1 or (len(str(no_i))==2 and (no_i//10)%10==1) or (len(str(no_i))==2 and (no_i%10==0)):
        return simple_dict[no_i]
    elif len(str(no_i))==2:
        return(f"{simple_dict[((no_i//10)%10)*10]}{simple_dict[(no_i%10)]}")
    else:
        if no_i%100==0:
            return(f"{simple_dict[no_i//100]} hundred")
        elif no_i%10==0 or (no_i%100)//10==1 or (no_i%100)//10==0:
            return(f"{simple_dict[no_i//100]} hundred {simple_dict[(no_i%100)]}")
        else:
            return(f"{simple_dict[no_i//100]} hundred {simple_dict[((no_i//10)%10)*10]}{simple_dict[(no_i%10)]}")  
    

def main():
   no=int(input("Your amount to be spelled please: "))

   print(write_no(no))

       

if __name__=="__main__":
    main()