"""


3. Center a String in the Terminal1
: Write a function that takes a string of characters as its
first parameter, and the width of the terminal in characters as its second parameter. Your
function should return a new string that consists of the original string and the correct
number of leading spaces so that the original string will appear centered within the provided
width when it is printed.
4. Capitalize It1
: Many people do not use capital letters correctly, especially when typing on
small devices like smart phones. In this exercise, you will write a function that capitalizes the
appropriate characters in a string. A lowercase “i” should be replaced with an uppercase “I” if
it is both preceded and followed by a space. The first character in the string should also be
capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the
function is provided with the string “what time do i have to be there? what’s the address?”
then it should return the string “What time do I have to be there? What’s the address?”.
Include a main program that reads a string from the user, capitalizes it using your function,
and displays the result.
5. Does a String Represent an Integer?1
: In this exercise you will write a function named
is_integer that determines whether or not the characters in a string represent a valid
integer. When determining if a string represents an integer you should ignore any leading or
trailing white space. Once this white space is ignored, a string represents an integer if its
length is at least 1 and it only contains digits, or if its first character is either + or - and the
first character is followed by one or more characters, all of which are digits. Write a main
program that reads a string from the user and reports whether or not it represents an
integer.
Hint: You may find the lstrip , rstrip and/or strip methods for strings helpful
when completing this exercise. Documentation for these methods is available online.
6. Only the Words1
: In this exercise you will create a program that identifies all of the words in
a string entered by the user. Begin by writing a function that takes a string of text as its only
parameter. Your function should return a list of the words in the string with the punctuation
marks at the edges of the words removed. The punctuation marks that you must remove
include commas, periods, question marks, hyphens, apostrophes, exclamation points,
colons, and semicolons. Do not remove punctuation marks that appear in the middle of a
words, such as the apostrophes used to form a contraction. For example, if your function is
provided with the string "Examples of contractions include: don’t, isn’t, and wouldn’t." then
your function should return the list ["Examples", "of", "contractions", "include", "don’t", "isn’t", "and", "wouldn’t"] . Write a main program that demonstrates your
function. It should read a string from the user and display all of the words in the string with
the punctuation marks removed.

"""