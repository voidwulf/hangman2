# Hangman

Hangman is a fun game to play on a console. This game lets users guess the words and letters with a funny hangman visual. Try and have fun! 

![cover_image](documentation/images/cover.JPG)

## Features

### Game flow

The game starts by initiating the code using the main function. Function get_word() retrieves a random word from an imported list of words. After the word has been received, the console introduces the game to the user, displaying a gallows visual and informing the user how many letters are in the target word.

The user enters either a word or a letter. IF a user enters a word, the word is checked if all characters are letters and if the number of letters is equal to the target word. If the conditions are satisfied, the word is compared with the target word. If the condition is not satisfied, user is informed that the input is incorrect and prompted to try to input a value again. When the word meets the If statement, conditions are compared with the target word if the answer is incorrect, the number of tries is reduced by 1. If the comment if correct the progression is updated to the maximal value.

In case the input is a single character, IF statement checks if the input is a letter. If the input is not a letter, user is informed that the input is incorrect and is prompted to try again. If the character is a letter, the letter is assessed if it has been used. If the letter has already been used, the user is informed that the letter has been used and input a different answer. If the letter has not been used yet in the game session, the letter is compared with the letters in the word. If the letter is in the word, the visuals and progression are updated, otherwise the number of tries is reduced by one. 

The process keeps repeating itself till the end game conditions have not been met. In this game, there are two end-game conditions. Firs condition is that the progression has achieved its maximum, e.g., the player has guessed the word, or the number of tries has been reduced to 0. If the player fills the progression to maximum, the user is greeted with the message that the game is won. If the player used his last try, he is greeted with the full and final hangman visual and informed that the game is lost and the target word. 

After the game has ended, the user is prompted to play another game. If the user answers Y, a new game is started. If the user answers N, the game ends.

![flowchart_part1](documentation/images/flowchart1.JPG)

![flowchart_part1](documentation/images/flowchart1.JPG)

### Visuals

In this game, there are used as part of the list.  The visuals are pulled based on the number of attempts. As the attempts are reduced, a new image of the hangman is pulled and replaces the previous one on the console. Each visual is designed in a funny way to have an additional funny comment in case the game is played by a younger audience.

Besides the visual display of the hangman, the console also informs the user how many words are in the game to avoid frustration with counting empty spaces. 

![final_visual](documentation/images/visuals1.JPG)

### Features to implement

* add option for user to chosse list of random words base on themes like music, history, movies, pop culture, memes etc.
* update the code to support multiple word questions
* implement object oriented programing for easier future work on the code


## Testing



## Deployment



## Cedits
