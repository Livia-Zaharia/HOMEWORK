""""
2. Two Word Random Password1
: While generating a password by selecting random
characters generally gives a relatively secure password, it also generally gives a password
that is difficult to memorize. As an alternative, some systems construct a password by taking
two words and concatenating them. While this password isn’t as secure, it is much easier to
memorize. Write a program that reads a file containing a list of words, randomly selects two
of them, and concatenates them to produce a new password. When producing the password
ensure that the total length is between 8 and 10 characters, and that each word used is at
least three letters long. Capitalize each word in the password so that the user can easily see
where one word ends and the next one begins. Display the password for the user.

"""

from pathlib import Path
import random

def string_prep(text):
    text=text.upper()
    text=text.replace('\n',' ')

    words=[]
    new_words=[]
    
    words=text.split()
    for word in words:
        if len(word)>4:
            if not word[-1].isalpha():
                new_word=word.rstrip(word[-1])
            else:
                new_word=word
        
            new_words.append(new_word)
        

    return new_words

    

def random_pass_generator(words:list)->str:
    
    while True:
        words_to_mix=random.sample(words,2)
        if (len(words_to_mix[0])+len(words_to_mix[1])>=8) and (len(words_to_mix[0])+len(words_to_mix[1])<=10):
            return words_to_mix[0].capitalize()+words_to_mix[1].capitalize()
 



def main():
   file_name= input("What file are you searching for?")
   
   p=Path.cwd()
   p0=p
   p=p/file_name
    
   if p in p0.glob("*"):
    
        
        with open(p,"r") as file_obj:
           lines_raw=file_obj.read()
        
        random_pass=random_pass_generator(string_prep(lines_raw))
        print(f"Your random pass is {random_pass}")

       
   else:
      print("there is no such file here")
           


       

if __name__=="__main__":
    main()