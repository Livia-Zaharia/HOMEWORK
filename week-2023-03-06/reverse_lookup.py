"""
1. Reverse Lookup1
: Write a function named reverse_lookup that finds all of the keys in a
dictionary that map to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from the
dictionary that map to the provided value. Include a main program that demonstrates the
reverse_lookup function as part of your solution to this exercise. Your program should
create a dictionary and then show that the reverse_lookup function works correctly when it
returns multiple keys, a single key, and no keys.

"""

def reverse_lookup(dict_to_check,value):
    return_values=[]
    for item in dict_to_check.items():
        if item[1]==value:
            return_values.append(item[0])
    return return_values


def main():
    my_dict={"A":"a","B":"b","C":"c","D":"a"}

    check_value=input("A value to search: ")
    print(reverse_lookup(my_dict,check_value))


if __name__=="__main__":
    main()