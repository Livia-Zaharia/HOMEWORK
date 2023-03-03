"""

3. Unique Characters1
: Create a program that determines and displays the number of unique
characters in a string entered by the user. For example, Hello, World! has 10 unique
characters while zzz has only one unique character. Use a dictionary to solve this problem.



"""
def chr_counting(words):
    global new_dict
    new_dict={}
    for letter in words:
        new_dict.setdefault(letter,0)
        new_dict[letter]+=1




def main():
   message=input("Your message please: ")

   chr_counting(message)
   print(len(new_dict.keys()))

       

if __name__=="__main__":
    main()