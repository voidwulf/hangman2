import random #import random module from library
from words import word_list #import list of words from words.py
from hangman_visual import stage # import hangman visual from hangman_visual.py

#inspired by https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python
def get_word():
    """
    function that retrives a random worl from list of words
    """
    word = random.choice(word_list)
    return word.upper()

def rungame():
    
    completion = False
    used_letters = []
    used_words = []


def hangman(tries):
    
    """
    Function that creates visual based on how many tries
    the user has left. Based on the remaining try, returnes
    visual value from the list

    return: stage visual as docstring
    """

    stage
    return stage [tries]