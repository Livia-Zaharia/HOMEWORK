"""

4. Anagrams Again1
: The notion of anagrams can be extended to multiple words. For example,
“William Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored. Extend your program from the exercise from class so that it is able to
check if two phrases are anagrams. Your program should ignore capitalization, punctuation
marks and spacing when making the determination.

"""


def chr_count(words):
    chr_dict={}
    for word in words:
        for letter in word:
            chr_dict.setdefault(letter,0)
            chr_dict[letter]+=1
    
    return chr_dict


def string_prep(text):
    text=text.upper()
    words=[]
    new_words=[]
    words=text.split()
    for word in words:
        if not word[-1].isalpha():
            new_word=word.rstrip(word[-1])
        else:
            new_word=word
        
        new_words.append(new_word)

    return new_words


def main():

   message_1=input("Your first message please: ")
   message_2=input("Your second message please: ")

   if (chr_count(string_prep(message_1))==chr_count(string_prep(message_2))):
       print ("the strings are anagrams")
   else:
       print("the strings are not anagrams")



       

if __name__=="__main__":
    main()