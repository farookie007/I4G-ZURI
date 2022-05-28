# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import string


def _filter_and_validate(word):
    "This function removes all the whhite spaces, symbols and punctuations in `word` sorts it and returns the result"
    word = word.lower().replace(' ', '')
    for letter in word:
        if not letter.isalnum():
            word = word.replace(letter, '')
    return ''.join(sorted(word))


def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = _filter_and_validate(word)
    anagram = _filter_and_validate(anagram)

    return word == anagram
