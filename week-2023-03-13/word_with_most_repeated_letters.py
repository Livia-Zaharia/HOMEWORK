"""

2. Word with most repeated letters:1
 Write a function, most_repeating_word , that takes a
sequence of strings as input. The function should return the string that contains the greatest
number of repeated letters. In other words:
For each word, find the letter that appears the most times.
Find the word whose most-repeated letter appears more than any other
"""


def most_repeating_word(word_list:list)->str:
    
    highest_no_of_letters_list=[]
    for word in word_list:
        letter_counter_dict={}
        for letter in word:
            letter_counter_dict.setdefault(letter,0)
            letter_counter_dict[letter]+=1
        values=list(letter_counter_dict.values())
        values.sort()
        highest_no_of_letters_list.append(values[-1])
    
    position_word=[]
    max_appeareances=max(highest_no_of_letters_list)

    for i, appearances in enumerate(highest_no_of_letters_list):
        if appearances==max_appeareances:
            position_word.append(word_list[i])
    

    print(f"there were {len(position_word)} words with {max_appeareances} max apperances of letters such as {' '.join(position_word)}")

    

def string_prep(text):
    text=text.lower()
    words=[]
    new_words=[]
    words=text.split()
    for word in words:
        if not word[-1].isalpha():
            new_word=word.rstrip(word[-1])
        else:
            new_word=word
        
        new_words.append(new_word)

    most_repeating_word(new_words)


def main():

   message=input("Your message please: ")

   string_prep(message)

       

if __name__=="__main__":
    main()