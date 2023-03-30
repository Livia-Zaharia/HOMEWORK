"""
1. Consistent Line Lengths1
: While 80 characters is a common width for a terminal window,
some terminals are narrow or wider. This can present challenges when displaying
documents containing paragraphs of text. The lines might be too long and wrap, making
them difficult to read, or they might be too short and fail to make use of the available space.
Write a program that opens a file and displays it so that each line is filled as full as possible. If
you read a line that is too long then your program should break it up into words and add
words to the current line until it is full. Then your program should start a new line and
display the remaining words. Similarly, if you read a line that is too short then you will need
to use words from the next line of the file to finish filling the current line of output. For
example, consider a file containing the following lines from “Alice’s Adventures in
Wonderland”:
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had nopictures or conversations in it,"and what is the use of a book," thought Alice, "without pictures or conversations?"
When formatted for a line length of 50 characters, it should be displayed as:
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice, "without pictures or conversations?"
Ensure that your program works correctly for files containing multiple paragraphs of text.
You can detect the end of one paragraph and the beginning of the next by looking for lines
that are empty once the end of line marker has been removed. You may perform error
checking if you want to, but it is not required for this exercise.

"""



from pathlib import Path

def split_words(text:str,no:int)->list:
    # text.replace('\n'," ")
    new_words=[]
    new_text=""
    t_len=0
    words=text.split(" ")

    for word in words:
        
        if (t_len+1)>=no:
            new_words.append(new_text)
            t_len=0
            new_text=word+" "
        else:
            new_text=new_text+word+" "
            t_len=t_len+len(word)+1
        
        if (words.index(word)==len(words)-1)and((t_len+1)<no):
            new_words.append(new_text)
 
    return new_words    



def split_paraghraph(text:str,no:int)->list:

    new_text=[]
    paragraphs=text.split('\n')
    for item in paragraphs:
        if len(item)>no:
            new_paragraph=split_words(item,no)
            for new_item in new_paragraph:
                new_text.append(new_item)
        else:
            new_text.append(item)

    return new_text
            


def main():
   file_name= input("What file are you searching for?")
   no=int(input("How many characters do you want to display/row?"))
   
   p=Path.cwd()
   p0=p
   p=p/file_name

   if p in p0.glob("*"):
    
        
        with open(p,"r") as file_obj:
           lines_raw=file_obj.read()
        
        text=split_paraghraph(lines_raw,no)
        
        print(len(text))
        for item in text:
             print(item)

       
   else:
      print("there is no such file here")
           


       

if __name__=="__main__":
    main()