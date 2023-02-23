"""4. Capitalize It1
: Many people do not use capital letters correctly, especially when typing on
small devices like smart phones. In this exercise, you will write a function that capitalizes the
appropriate characters in a string. A lowercase “i” should be replaced with an uppercase “I” if
it is both preceded and followed by a space. The first character in the string should also be
capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the
function is provided with the string “what time do i have to be there? what’s the address?”
then it should return the string “What time do I have to be there? What’s the address?”.
Include a main program that reads a string from the user, capitalizes it using your function,
and displays the result."""



def check_symbol(word):
    if word[-1].isalpha():
        return False
    return True


def reconstruct():
    cap=0
    new_words=[]
    for word in words:
        if cap==1 or word=="i":
            new_words.append(word.capitalize())
            cap=0
        else:
            new_words.append(word)
        
        if check_symbol(word):
            cap=1
        
    return " ".join(new_words)


def process_input_phrase():
    text=input("Spell check text: ")
    text=text.lower()
    text=text.capitalize()
    global words
    words=text.split(" ")



def main():
    process_input_phrase()
    print(reconstruct())  

    
        





if __name__=="__main__":
    main()