import csv 
import string

def read_wrods_from_file(file_name):
    words = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            words.extend(row)

        return words
    
def calculate_word_value(word):
    uppercase_word = word.upper()
    letter_values = {letter: index + 1 for index, letter in enumerate(string.ascii_uppercase)}
    return sum(letter_values[letter] for letter in uppercase_word)

def is_triangle_number(number):
    n = int(((8 * number + 1) ** 0.5 - 1) / 2)
    return n * (n + 1) == 2 * number

words = read_wrods_from_file('words.txt')

traingle_words_count = 0
for word in words:
    word_value = calculate_word_value(word)
    if is_triangle_number(word_value):
        traingle_words_count += 1

print(f"The number of traingle words in the file is: {traingle_words_count}")
