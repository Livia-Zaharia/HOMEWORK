


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