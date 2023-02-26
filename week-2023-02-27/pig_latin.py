


def vowel_processing(word):
    return word+"way"

def consonant_processing(word):
    for letter in word:
        if letter in vowels:
            return word[word.index(letter):]+word[:word.index(letter)]+"ay"


def word_check(words):
     check_punct=0
     check_upper=0
     new_words=[]

     for word in words:
         

         if not (word[-1].isalpha()):
             punctuation=word[-1]
             word=word[:-1]
             check_punct=1

         if word[0].isupper():
             check_upper=1
             word=word.lower()

         if word[0] in vowels:
             word=vowel_processing(word)
         else:
             word=consonant_processing(word)

         if check_punct==1:
             word=word+punctuation
             check_punct=0

         if check_upper==1:
             word=word.capitalize()
             check_upper=0

         new_words.append(word)

     return new_words



def main():
    global vowels
    vowels=['a','e','i','o','u']
    words=[]

    phrase=input("What phrase you want converted?  ")
            
    words=phrase.split(" ")
    returned_words=word_check(words)
    returned_phrase=" ".join(returned_words)

    print(returned_phrase)




if __name__=="__main__":
    main()