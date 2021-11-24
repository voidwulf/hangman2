import random  # import random module from library
from words import word_list  # import list of words from words.py
from hangman_visual import stage  # import hangman visual

# inspired by:
# https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python


def get_word():
    """
    function that retrives a random worl from list of words

    return: string in capitals
    """
    word = random.choice(word_list)
    return word.upper()

# inspired by:
# https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python
# and https://github.com/kying18/hangman/blob/master/hangman.py


def rungame(word):
    """
    Function that sets start condition of the game, iterates
    the game by setting a number of letters from a random word,
    chacking users input and comparing if the answer correct.
    Function is also validating user input in case in case of
    wrong data entered number or to many/few letters in a guess
    word
    """
    completion = False
    letters = set(word)
    used_letters = []
    used_words = []
    tries = 7
    progress = "_" * len(word)

    print("Let's play Hangman!")
    print(hangman(tries))
    print(progress)
    print("\n")

    while tries > 0 and not completion:
        print("This word contains", len(word), "letters.")
        answer = input("Please guess a letter or word: \n").upper()
        if len(answer) == len(word) and answer.isalpha():
            if answer == word:
                completion = True
                progress = word
            elif answer in used_words:
                print("You already used the word", answer)
            else:
                print(answer, "is not the word.")
                tries -= 1
                used_words.append(answer)
        elif len(answer) == 1 and answer.isalpha():
            if answer in used_letters:
                print("You already used the letter", answer)
            elif answer in letters:
                print("Good job,", answer, "is in the word!")
                used_letters.append(answer)
                prog = list(progress)
                indi = [i for i, letter in enumerate(word) if letter == answer]
                for index in indi:
                    prog[index] = answer
                progress = "".join(prog)
                if "_" not in progress:
                    completion = True
            else:
                print(answer, "is not in the word.")
                tries -= 1
                used_letters.append(answer)
        else:
            # warn user that the input is invalid
            print("Invalid guess.Please gues a letter or word.")
        print(hangman(tries))
        print(progress)
        print("\n")
    if progress:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ".")


def hangman(tries):

    """
    Function that creates visual based on how many tries
    the user has left. Based on the remaining try, returnes
    visual value from the list

    return: stage visual as docstring
    """

    stage
    return stage[tries]

# inspired by
# https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python


def main():

    """
    Main function that executes the code

    """

    word = get_word()
    rungame(word)
    while input("Play Again? (Y/N) \n").upper() == "Y":
        word = get_word()
        rungame(word)
    else:
        print("Thank you for playing, hope to see you again! :)")


if __name__ == "__main__":
    main()
