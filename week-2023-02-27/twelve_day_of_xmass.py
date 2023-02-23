"""
2. The Twelve Days of Christmas1
: The Twelve Days of Christmas is a repetitive song that
describes an increasingly long list of gifts sent to one’s true love on each of 12 days. A single
gift is sent on the first day. A new gift is added to the collection on each additional day, and
then the complete collection is sent. The first three verses of the song are shown below. The
complete lyrics are available on the internet.
On the first day of Christmas
my true love sent to me:
A partridge in a pear tree.
On the second day of Christmas
my true love sent to me:
Two turtle doves,
And a partridge in a pear tree.
On the third day of Christmas
my true love sent to me:
Three French hens,
Two turtle doves,
And a partridge in a pear tree
Your task is to write a program that displays the complete lyrics for The Twelve Days of
Christmas. Write a function that takes the verse number as its only parameter and displays
the specified verse of the song. Then call that function 12 times with integers that increase
from 1 to 12. Import your solution to Exercise 1 to help you complete this exercise.

"""




"""
On the twelfth day of Christmas
My true love sent to me
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three French hens
Two turtle doves and
A partridge in a pear tree
"""


import ordinal_name

def gift_calling(number:int)->str:
    return_gifts=[]
    gifts=["A partridge in a pear tree","Two turtle doves","Three French hens","Four calling birds","Five golden rings","Six geese a-laying","Seven swans a-swimming","Eight maids a-milking","Nine ladies dancing","Ten lords a-leaping","Eleven pipers piping","Twelve drummers drumming"]
    for i in range((number-1),0,-1) :
        return_gifts.append(gifts[i])
    return_gifts.append("a partridge in a pear tree")
    if number==1:
        return gifts[0]
    elif number==2:
        return "\nAnd ".join(return_gifts)
    else:
        return ',\n'.join(return_gifts[0:-2])+',\n'+"\nAnd ".join(return_gifts[-2:])
    
        
    
def verse_forming(number:int)->str:
    day_number=ordinal_name.ordinal_name(number)
    space='\n'
    gifts=gift_calling(number)
    base_call=f"On the {day_number} day of Christmas{space}My true love sent to me{space}{gifts}"
    song_lyrics.append(base_call)


def main():
    global song_lyrics
    song_lyrics=[]

    for i in range(1,13):
        verse_forming(i)

    querry_verse=int(input("What verse would you like to read first? "))
    print('\n')
    print(song_lyrics[querry_verse-1])
    
    print ('\nAnd now for the complete version...\n')
    for i in song_lyrics:
        print("\n")
        print (i)


if __name__=="__main__":
    main()