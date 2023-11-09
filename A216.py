from collections import defaultdict

def load_word_list(url):
    import requests
    response = requests.get(url)
    words = response.text.splitlines()
    return words

def find_anagrams(word_list):
    anagrams = defaultdict(list)
    for word in word_list:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return anagrams

def find_anagram_set(word, anagram_dict):
    key = ''.join(sorted(word))
    return anagram_dict.get(key, [])

url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'

word_list = load_word_list(url)

anagagram_sets = find_anagrams(word_list)

max_size = max(len(words) for words in anagagram_sets.values())
largest_anagrams = [words for words in anagagram_sets.values() if len(words) == max_size]

for anagram_set in largest_anagrams:
    print(anagram_set)