from math import floor
from sys import maxsize
word = input()
strongest_word_sum = -maxsize
strongest_word = ""
first_letter = ""
while word != "End of words":
    ascii_sum = 0
    total_ascii_sum = 0
    for letter in word:
        ascii_sum = 0
        letter_ascii = ord(letter)
        ascii_sum = ascii_sum + letter_ascii
        total_ascii_sum = total_ascii_sum + ascii_sum
    if word[0] in word == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" or word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
        total_ascii_sum = total_ascii_sum * len(word)
    else:
        total_ascii_sum = floor(total_ascii_sum / len(word))
    if total_ascii_sum > strongest_word_sum:
        strongest_word_sum = total_ascii_sum
        strongest_word = word
    word = input()

print(f"The most powerful word is {strongest_word} - {strongest_word_sum}")
