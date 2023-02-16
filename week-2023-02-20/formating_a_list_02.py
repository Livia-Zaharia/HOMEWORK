"""
2. Formatting a List1
: When writing out a list of items in English, one normally separates the
items with commas. In addition, the word “and” is normally included before the last item,
unless the list only contains one item. Consider the following four lists:
apples apples and oranges apples, oranges and bananas apples, oranges, bananas and lemons
Hint: You can concatenate the strings until the last one using the comma as the separator
and add the "and" for the last one. Optionally, you can do the concatenation with the join
string method. join is used with the separator as the string that calls the join method .
For example we can have ", ".join(["apples", "oranges", "banana"]) that creates the
string "apples, oranges, banana" . More at https://docs.python.org/3/library/stdtypes.ht
ml#str.join

"""
def concat_comma():
    if len(word_list)==2:
        return " and ".join(word_list)
    else:
        return ", ".join(word_list[0:-2])+", "+" and ".join(word_list[-2:])

def read():
    global word_list
    word_list=[]
    while True:
        word=input("New word you want in: ")
        if word=="":
            break
        word_list.append(word)


def main():
    read()
    print(concat_comma())
   

if __name__=="__main__":
    main()