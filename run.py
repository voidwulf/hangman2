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
    letters = set(word)
    used_letters = []
    used_words = []
    tires = 7
    progress = "_" * len(word)

    print("Let's play Hangman!")
    print(hangman(tries))
    print(word_completion)
    print("\n")

    while tries > 0 and not completion:
        print("This word contains", len(word_lenght), "letters.") 
        answer = input("Please guess a letter or word: \n").upper() 
        if len(answer) == len(word) and answer.isalpha():
            if  answer == word:
                completion = True
                progress = word       
            elif answer in used_words:
                print("You already used the word", answer)
            else:
               print(guess, "is not the word.")
               tries -= 1
               guessed_words.append(answer) 






def hangman(tries):
    
    """
    Function that creates visual based on how many tries
    the user has left. Based on the remaining try, returnes
    visual value from the list

    return: stage visual as docstring
    """

    stage
    return stage [tries]