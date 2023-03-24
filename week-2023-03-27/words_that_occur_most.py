""""
1. Words that Occur Most1
: Write a program that displays the word (or words) that occur
most frequently in a file. Your program should begin by reading the name of the file from the
user. Then it should find the word(s) by splitting each line in the file at each space. Finally,
any leading or trailing punctuation marks should be removed from each word. In addition,
your program should ignore capitalization. As a result, apple, apple!, Apple and ApPlE should
all be treated as the same word.

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


def words_counting(text:str)->dict:
    words=string_prep(text)
    no_of_words={}

    for word in words:
        no_of_words.setdefault(word,0)
        no_of_words[word]+=1

    return no_of_words
    

def ordering_by_value(dict_words:dict)->list:
    
    sorted_values=list(dict_words.values())
    sorted_values.sort()
    print(len(sorted_values))
    sorted_list=[0]*len(sorted_values)
    for k,v in list(dict_words.items()):
        
        sorted_list[sorted_values.index(v)]=(k,v)
        sorted_values[sorted_values.index(v)]=0

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
        
        ordering_by_value(words_counting(lines_raw))

       
   else:
      print("there is no such file here")
           


       

if __name__=="__main__":
    main()