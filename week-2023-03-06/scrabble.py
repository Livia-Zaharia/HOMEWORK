"""

5. Scrabble™ Score1
: In the game of Scrabble™, each letter has points associated with it. The
total score of a word is the sum of the scores of its letters. More common letters are worth
fewer points while less common letters are worth more points. The points associated with
each letter are shown below:
Write a program that computes and displays the Scrabble™ score for a word. Create a
dictionary that maps from letters to point values. Then use the dictionary to compute the
score.


"""



def scrabble_value(word):
    word_value=0
    for letter in word:
            word_value+=scrabble_dict[letter]
               
    return word_value


def main():
   global scrabble_dict
   scrabble_dict={
       "A":1, "B":3, "C":3, "D":2,
       "E":1, "F":4, "G":2, "H":4,
       "I":1, "J":8, "K":5, "L":1,
       "M":3, "N":1, "O":1, "P":3,
       "Q":10, "R":1, "S":1, "T":1,
       "U":1, "V":4, "W":4, "X":8,
       "Y":4, "Z":10
   }
   word=input("Your word please: ")
   word=word.upper()

   print("Scrabble value of"+str(scrabble_value(word)))


       

if __name__=="__main__":
    main()