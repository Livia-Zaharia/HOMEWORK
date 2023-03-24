from pathlib import Path


def main():
   file_name= input("What file are you searching for?")
   
   p=Path.cwd()
   p0=p
   p=p/file_name
    
   

   if p in p0.glob("*"):
    
        
        with open(p,"r") as file_obj:
           lines_raw=file_obj.read()
        
        text_lines=lines_raw.split("\n")

        new_name=input("new file name")+".txt"
        p2=p0/new_name

        file_obj2=open(p2,"x")
        file_obj2.close()

        with open(p2,"w",) as file_obj2:
           for index,line in enumerate(text_lines):
            file_obj2.write(f"{index}, {line}\n")
          


       

if __name__=="__main__":
    main()