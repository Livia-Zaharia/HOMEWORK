


def ubbi_dubbi_translate(word:str)->str:
    vowels="aeiou"
    word.lower()
    new_word=word
    for letter in vowels:
        if letter in word:
            check=True
            last_half=new_word[new_word.index(letter):]
            first_half=new_word[:new_word.index(letter)]
            while check:
                new_word=first_half+'ub'+last_half
                if letter not in last_half:
                    check=False
                else:
                    last_half=last_half[last_half.index(letter):]
                    first_half=first_half+"ub"+letter


def main():
   word=input("Your word to be translated please: ")

   print(ubbi_dubbi_translate(word))

       

if __name__=="__main__":
    main()