from pathlib import Path


def lines_counting(text:str)->list:
    global text_lines
    text_lines=text.split("\n")
    return len(text_lines)


def main():
   file_name= input("What file are you searching for?")
   
   p=Path.cwd()
   p0=p
   p=p/file_name
    
   

   if p in p0.glob("*"):
    
        
        file_obj=open(p,"r")
        lines_raw=file_obj.read()
        file_obj.close()

        no_lines_infile=lines_counting(lines_raw)

        no_of_lines=int(input("How many lines do you want read?"))
        head_tail=int(input("Do you want to read the head (0) or the tail (1)?"))

        if no_lines_infile<no_of_lines:
           print(f"The file has only {no_lines_infile} line. Please reconsider")
        else:
           if head_tail==0:
              for i in range(no_of_lines):
                 print(text_lines[i])
           elif head_tail ==1:
              for i in range(no_of_lines+1):
                 print(text_lines[no_lines_infile-i-1])
           else:
              print("It is either from the start or from the end- can't be in between")
   else:
      print("there is no such file here")
           


       

if __name__=="__main__":
    main()