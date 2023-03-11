""""
 Postal Codes2
: In a Canadian postal code, the first, third and fifth characters are letters while
the second, fourth and sixth characters are numbers. The province can be determined from
the first character of a postal code, as shown in the following table. No valid postal codes
currently begin with D, F, I, O, Q, U, W, or Z.
The second character in a postal code identifies whether the address is rural or urban. If that
character is a 0 then the address is rural. Otherwise it is urban. Create a program that reads
a postal code from the user and displays the province associated with it, along with whether
the address is urban or rural. For example, if the user enters T2N 1N4 then your program
should indicate that the postal code is for an urban address in Alberta. If the user enters X0A
1B2 then your program should indicate that the postal code is for a rural address in Nunavut
or Northwest Territories. Use a dictionary to map from the first character of the postal code
to the province name. Display a meaningful error message if the postal code begins with an
invalid character.

"""

def check_code(text:str):
    text=text.replace(" ","")
    if len(text)!=6:
        return("invalid format- postal code requires 6 characters")
    if text[0].isalpha()== False or text[2].isalpha()== False or text[4].isalpha()== False or text[1].isdigit()== False or text[3].isdigit()== False or text[5].isdigit()== False:
        return("invalid format- postal code must have first, third and fifth characters as letters and the rest numeric")
    if text[0] in region_code.keys():
        if int(text[1])==0:
            return(f"code from a rural adress in {region_code[text[0]]}")
        else:
            return(f"code from an urban adress in {region_code[text[0]]}")
    else:
        return ("invalid region character")


def main():
   global region_code
   region_code={
       "A":"Newfoundland", "B":"Nova Scotia", "C":"Prince Edward Island",
       "E":"New Brunswick", "G":"Quebec", "H":"Quebec", "J":"Quebec",
       "K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario",
       "R":"Manitoba", "S":"Saskatchewan", "T":"Alberta",
       "V":"British Columbia", "X":"Nunanvut and Northwest territories",
       "Y":"Yukon"
   }
   code=input("Your postal code to be checked: ")
   print(check_code(code))



       

if __name__=="__main__":
    main()