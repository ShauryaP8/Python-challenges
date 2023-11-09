def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for letter in word if letter in vowels)

word = str(input("Enter your word: "))
print(f"The word '{word}' has {count_vowels(word)} vowels")