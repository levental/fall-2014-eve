
#EX 25

def break_words(stuff):
    """this is a function that will break up words for you"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort the words"""
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it off"""
    word = words.pop(0)
    print word

def print_first_word(words):
    """print the last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """take in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_first_last(words)

def print_firstandlast_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

words = "now missing The remaining lines are for you to figure out and analyze in the extra credit."


