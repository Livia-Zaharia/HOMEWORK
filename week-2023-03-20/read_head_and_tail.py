from pathlib import Path
import os


def lines_counting(text:str)->list:
    global text_lines
    text_lines=text.split("\n")
    return len(text_lines)


def main():
   file_name= input("What file are you searching for?")
   p_os=os.getcwd()
   print(p_os)
   p=Path.cwd()
   p=p/file_name
   file_obj=open(p,"r")
   lines_raw=file_obj.read()
   file_obj.close()

   no_lines_infile=lines_counting(lines_raw)

   no_of_lines=int(input("How many lines do you want read?"))

   for i in range(no_of_lines):
       print(text_lines[i])


       

if __name__=="__main__":
    main()