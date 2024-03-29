"""

3. Unique Characters1
: Create a program that determines and displays the number of unique
characters in a string entered by the user. For example, Hello, World! has 10 unique
characters while zzz has only one unique character. Use a dictionary to solve this problem.



"""
def chr_counting(words):
    global new_dict
    new_dict={}
    for word in words:
        for letter in word:
            new_dict.setdefault(letter,0)
            new_dict[letter]+=1


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

    chr_counting(new_words)



def main():
   message=input("Your message please: ")

   string_prep(message)
   print(len(new_dict.keys()))

       

if __name__=="__main__":
    main()