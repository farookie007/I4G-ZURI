# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string


def read_file_content(filename):
    # [assignment] Add your code here 

    with open(filename, 'r') as f:
        content = f.read()
    
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    word_count = dict()
    words = text.lower().split()

    for word in words:
        word = _strip_punctuation(word)
        if not word_count.get(word):
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count


def _strip_punctuation(word: str) -> str:
    """
    This function strips every punctuation surrounding `word` and returns the word
    :params: str;
    :return: str;
    Example: ",!;woflal..dffj....!" -> 'woflal..dffj', "wouldn't" -> "wouldn't"
    """
    first, last = word[0], word[-1]
    punctuations = string.punctuation

    if not((first in punctuations) or (last in punctuations)):   # checking if the first and last letters are punctuations and subsequently strips them off 
        return word
    elif (first in punctuations):
        return _strip_punctuation(word[1:])
    else:
        return _strip_punctuation(word[:-1])
