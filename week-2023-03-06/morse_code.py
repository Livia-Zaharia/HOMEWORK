"""
2. Morse Code1
: Morse code is an encoding scheme that uses dashes and dots to represent
numbers and letters. In this exercise, you will write a program that uses a dictionary to store
the mapping from letters and numbers to Morse code. Use a period to represent a dot, and
a hyphen to represent a dash. The mapping from letters and numbers to dashes and dots is
shown in Table 6.1. Your program should read a message from the user. Then it should
translate each letter and number in the message to Morse code, leaving a space between
each sequence of dashes and dots. Your program should ignore any characters that are not
letters or numbers. The Morse code for Hello, World! is shown below:
.... . .-.. .-.. --- .-- --- .-. .-.. -..

"""
def to_morse(words):
    morse_message=[]
    for word in words:
        for letter in word:
            morse_message.append(morse_dict[letter])
    
    morse=" ".join(morse_message)
    print(morse)

    # for morse in morse_message:
    #     print(morse)


def string_prep(text):
    text=text.upper()
    words=[]
    new_words=[]
    words=text.split()
    for word in words:
        if not word[-1].isalpha():
            new_word=word.rstrip(word[-1])
        else:
            new_word=word
        
        new_words.append(new_word)

    to_morse(new_words)


def main():
   global morse_dict
   morse_dict={
       "A":".-", "B":"-...", "C":"-.-.", "D":"-..",
       "E":".", "F":"..-.", "G":"--.", "H":"....",
       "I":"..", "J":".---", "K":"-.-", "L":".-..",
       "M":"--", "N":"-.", "O":"---", "P":".--.",
       "Q":"--.-", "R":".-.", "S":"...", "T":"-",
       "U":"..-", "V":"...-", "W":".--", "X":"-..-",
       "Y":"-.--", "Z":"--..", "0":"-----", "1":".----",
       "2":"..---", "3":"...--", "4":"....-", "5":".....",
       "6":"-....", "7":"--...", "8":"---..", "9":"----."
   }
   message=input("Your message please: ")

   string_prep(message)
   

if __name__=="__main__":
    main()