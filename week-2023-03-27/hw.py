""""
1. Words that Occur Most1
: Write a program that displays the word (or words) that occur
most frequently in a file. Your program should begin by reading the name of the file from the
user. Then it should find the word(s) by splitting each line in the file at each space. Finally,
any leading or trailing punctuation marks should be removed from each word. In addition,
your program should ignore capitalization. As a result, apple, apple!, Apple and ApPlE should
all be treated as the same word.
2. Two Word Random Password1
: While generating a password by selecting random
characters generally gives a relatively secure password, it also generally gives a password
that is difficult to memorize. As an alternative, some systems construct a password by taking
two words and concatenating them. While this password isn’t as secure, it is much easier to
memorize. Write a program that reads a file containing a list of words, randomly selects two
of them, and concatenates them to produce a new password. When producing the password
ensure that the total length is between 8 and 10 characters, and that each word used is at
least three letters long. Capitalize each word in the password so that the user can easily see
where one word ends and the next one begins. Display the password for the user.
3. A Book with No “e” …1
: The novel “Gadsby” is over 50,000 words in length. While 50,000
words isn’t normally remarkable for a novel, it is in this case because none of the words in
the book use the letter “e”. This is particularly noteworthy when one considers that “e” is the
most common letter in English. Write a program that reads a list of words from a file and
determines what proportion of the words use each letter of the alphabet. Display the result
for all 26 letters. Include an additional message identifying the letter that is used in the
smallest proportion of the words. Your program should ignore any punctuation marks and it
should treat uppercase and lowercase letters as equivalent.
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