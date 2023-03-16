from pathlib import Path

def reverse_reading(p:Path,no_of_lines:int):
   with open(p,"rb") as file_obj:
      
      no_of_lines_read=0
      file_obj.seek(0,2)
      i=file_obj.tell()
      j=-1

      while no_of_lines_read!=no_of_lines+1:
         file_obj.seek(j,2)
         
         if file_obj.read(1).decode("utf-8")=="\n":
            no_of_lines_read+=1
      
         j-=1
      
      file_obj.seek(file_obj.tell())
      print(file_obj.read().decode("utf-8"))

def normal_reading(p:Path, no_of_lines:int):
    lines_list=[]

    with open(p,"r") as file_obj:
      for i in range(no_of_lines):
         lines_list.append(file_obj.readline())
         
    for line in lines_list:
      line=line.strip("\n")
      print(line)

def main():
   file_name= input("What file are you searching for?")
   
   p=Path.cwd()
   p0=p
   p=p/file_name
    
   if p in p0.glob("*"):
      no_of_lines=int(input("How many lines do you want read?"))
      head_tail=int(input("Do you want to read the head (0) or the tail (1)?"))
      
      if head_tail==0:
        normal_reading(p,no_of_lines)
      elif head_tail ==1:
           reverse_reading(p,no_of_lines)
         
      else:
         print("It is either from the start or from the end- can't be in between")
   else:
      print("there is no such file here")
           


       

if __name__=="__main__":
    main()