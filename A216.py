from collections import defaultdict

def find_anagrams(word_list):
    anagram_groups = defaultdict(list)

    # Group words by their sorted characters
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    # Find the groups with the most words
    max_group_size = max(len(group) for group in anagram_groups.values())
    max_groups = [group for group in anagram_groups.values() if len(group) == max_group_size]

    return max_groups

if __name__ == '__main__':
    # Read the word list from the provided URL
    import urllib.request
    url = 'https://gist.githubusercontent.com/jamesabela/d956da0889582e5c5c8fc34ed72b97c3/raw/6ef9a8845bf42de2ce1e51d7f70c72f0d8333526/wordlist.txt'
    word_list = urllib.request.urlopen(url).read().decode().split()

    # Find anagrams for a given word
    input_word = input("Enter a word to find its anagrams: ").lower()
    groups = find_anagrams(word_list)

    anagram_groups = [group for group in groups if input_word in group]
    if anagram_groups:
        print(f"The word '{input_word}' has the following anagrams:")
        for group in anagram_groups:
            print(group)
    else:
        print(f"No anagrams found for the word '{input_word}'.")
