""""
4. Construction work ahead: Attached to this file you will find a JSON file called
mock_construction_data.json . Your task is to extract the following:
1. How many records are in the file?
2. How many of the records are missing their email, in percentages?
3. How many of the records are missing their company, in percentages?
4. How many records are of people being managers?
5. [Optional] Find and group records that are working for the same company. You can
consider those that have their company missing as working for the same company.
6. [Optional] Sort the records by the years of experience.
7. [Optional] Find and group records that are sharing the same job title and save them in
separate JSON files.

"""


from pathlib import Path
import json

def group_all_data_by_attribute(data:list,key:str):
   categories=extract_unique_attributes(data,key)
   categories.sort()
   
   grouped_list=[]
   
   for item in categories:
     values=group_by_attribute(data,key,item)
     grouped_list.append(values)

   return grouped_list
   
def group_by_attribute(data:list,key:str,value):
      group_dict={}
      
      for item in data:
         if type(value)!=str :
            if item[key]==value:
               group_dict.setdefault(value,[])
               group_dict[value].append(item)

         elif value=="None":
            if item[key]==None:
               group_dict.setdefault(value,[])
               group_dict[value].append(item)
         
         else:
            if value == item[key]:
               group_dict.setdefault(value,[])
               group_dict[value].append(item)
      
      return group_dict

def extract_unique_attributes(data:list, key:str):
   list_of_atr=[]
   for item in data:
      if item[key]==None:
         new="None"
      else:
         new=item[key]

      list_of_atr.append(new)
   
   list_of_atr=set(list_of_atr)
   list_of_atr=list(list_of_atr)

   return list_of_atr
   
def search_for_atributes(data:list,key:str,value)->int:
      count=0
      for item in data:
         if type(value)!=str :
            if item[key]==value:
               count+=1
         else:
            if value in item[key]:
               count+=1
      return count

def main():
   with open("mock_construction_data.json","r") as file:
    data= json.load(file)


   no=len(data)

   print(f"there are {no} records in the file")
   missing_email=(search_for_atributes(data,"email",None)/no)*100
   missing_email=round(missing_email,2)
   missing_company=(search_for_atributes(data,"company_name",None)/no)*100
   missing_company=round(missing_company,2)
   
   print(f"there are {missing_email} % entries missing emails")
   print(f"there are {missing_company} % entries missing company")
   no_managers=(search_for_atributes(data,"job_title","Manager")/no)*100
   no_managers=round(no_managers,2)
   print(f"there are {no_managers} % entries with manager jobs")

   
   
   grouped_list=group_all_data_by_attribute(data,"company_name")
   
   for item in grouped_list:
      print(item)
      print('\n')


   
   grouped_list_y=group_all_data_by_attribute(data,"years_of_experience")
   
   for item in grouped_list_y:
      print(item)
      print('\n')

   
   grouped_list_j=group_all_data_by_attribute(data,"job_title")
   
   
   for item in grouped_list_j:
    with open(f"{list(item.keys())[0]}.json","w") as file:
       json.dump(item,file)
   
         

if __name__=="__main__":
    main()