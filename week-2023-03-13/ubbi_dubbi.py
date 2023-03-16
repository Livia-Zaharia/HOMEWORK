
"""
1. Ubbi Dubbi1
: In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk
becomes mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am). For this
exercise, you’ll write a function (called ubbi_dubbi ) that takes a single word (string) as an
argument. It returns a string, the word’s translation into Ubbi Dubbi. So if the function is
called with octopus , the function will return the string uboctubopubus . And if the user
passes the argument elephant , you’ll output ubelubephubant .

"""

# could have been written using replace method of strings.

def ubbi_dubbi_translate(word:str)->str:
    vowels="aeiou"
    word.lower()
    position=[]
    
    
    for letter_v in vowels:
        if letter_v in word:
            for no,letter in enumerate(word):
                if letter_v==letter:
                    position.append(no)

    position.sort()
    
    prev_index=0
    new_word=""
    for index_value in position:
        new_word=new_word+word[prev_index:index_value]+"ub"
        prev_index=index_value

    new_word+=word[prev_index:]

    return new_word
        

def main():
   word=input("Your word to be translated please: ")

   print(ubbi_dubbi_translate(word))

       

if __name__=="__main__":
    main()