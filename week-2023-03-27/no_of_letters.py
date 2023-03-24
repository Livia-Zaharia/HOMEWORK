""""
3. A Book with No “e” …1
: The novel “Gadsby” is over 50,000 words in length. While 50,000
words isn’t normally remarkable for a novel, it is in this case because none of the words in
the book use the letter “e”. This is particularly noteworthy when one considers that “e” is the
most common letter in English. Write a program that reads a list of words from a file and
determines what proportion of the words use each letter of the alphabet. Display the result
for all 26 letters. Include an additional message identifying the letter that is used in the
smallest proportion of the words. Your program should ignore any punctuation marks and it
should treat uppercase and lowercase letters as equivalent.


"""

from pathlib import Path

def string_prep(text):
    text=text.upper()
    text=text.replace('\n',' ')

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


def letter_counting(text:str)->dict:
    words=string_prep(text)
    letters={}
    for word in words:
        for letter in word:
            letters.setdefault(letter,[])
            letters[letter].append(word)

    for item in list(letters.keys()):
        letters[item]=set(letters[item])

    return letters
    

    

def ordering_by_value(dict_l:dict)->list:
    sorted_values=[]
    sorted_values_sets=list(dict_l.values())
   
    for item in sorted_values_sets:
        sorted_values.append(len(item))

    sorted_values.sort()
    
    sorted_list=[0]*len(sorted_values)
    for k,v in list(dict_l.items()):
        
        sorted_list[sorted_values.index(len(v))]=(k,len(v))
        sorted_values[sorted_values.index(len(v))]=0

    for item in sorted_list:
        k,v= item
        print(k,"-",v)



def main():
   file_name= input("What file are you searching for?")
   
   p=Path.cwd()
   p0=p
   p=p/file_name
    
   

   if p in p0.glob("*"):
    
        
        with open(p,"r") as file_obj:
           lines_raw=file_obj.read()
        
        ordering_by_value(letter_counting(lines_raw))

       
   else:
      print("there is no such file here")
           


       

if __name__=="__main__":
    main()