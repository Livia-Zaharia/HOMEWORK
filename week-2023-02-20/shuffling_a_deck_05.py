"""
5. Shuffling a Deck of Cards1
: A standard deck of playing cards contains 52 cards. Each card
has one of four suits along with a value. The suits are normally spades, hearts, diamonds and
clubs while the values are 2 through 10, Jack, Queen, King and Ace. Each playing card can be
represented using two characters. The first character is the value of the card, with the values
2 through 9 being represented directly. The characters “T”, “J”, “Q”, “K” and “A” are used to
represent the values 10, Jack, Queen, King and Ace respectively. The second character is used
to represent the suit of the card. It is normally a lowercase letter: “s” for spades, “h” for
hearts, “d” for diamonds and “c” for clubs. The following table provides several examples of
cards and their two-character representations.
Begin by writing a function named create_deck . It will use loops to create a complete deck
of cards by storing the two-character abbreviations for all 52 cards into a list. Return the list
of cards as the function’s only result. Your function will not take any parameters.
Write a second function named shuffle that randomizes the order of the cards in a list.
One technique that can be used to shuffle the cards is to make use of Python’s
random.shuffle function. Use both of the functions described in the previous paragraphs
to create a main program that displays a deck of cards before and after it has been shuffled.
Hint: https://www.w3schools.com/python/ref_random_shuffle.asp

"""

import random
import copy

def create_deck():
    list_numbers=[]
    for i in range(2,10):
        list_numbers.append(str(i))
    list_special_case=["T", "J", "Q", "K", "A"]
    list_numbers.extend(list_special_case)
    
    global complete_deck
    complete_deck=[]

    list_packs=["s","h","d","c"]
    for pack in list_packs:
        for elem in list_numbers:
            complete_deck.append(pack+elem)

    print("Original deck")
    nice_output(complete_deck)




def shuffle_deck():
    shuffled_deck=copy.deepcopy(complete_deck)
    random.shuffle(shuffled_deck)
    print("After shuffle")
    nice_output(shuffled_deck)

def nice_output(misc_list):
    
    for elem in misc_list:
        print(elem)

def main():
    create_deck()
    shuffle_deck()
    

if __name__=="__main__":
    main()