import random
from stages import stages

word_list = ["aardvark", "baleia", "camelo", "doninha", "elefante",
             "flamingo", "galinha", "hiena", "iguana", "jararaca",
             "kiwi", "lince", "morsa", "narval", "ovelha", "papagaio",
             "quati", "rinoceronte", "suricate", "tartaruga", "urso",
             "vagalume", "wallaby", "ximango", "yak", "zebra"]


chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

# checking if the word matches
for letter in chosen_word:
    if letter == guess:
        print("Guess")
    else:
        print("Fail")
"""
#     Creating an empty List called display.
#     For each letter in the chosen_word, adding a "_" to 'display'.
#     So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]
#     with 5 "_" representing each letter to guess. """


display = []
for letter in range(len(chosen_word)):
    display += "_"

#  Looping through each position in the chosen_word;
#  If the letter at that position matches 'guess' then reveal that letter in the
#  display at that position.
#  e.g. If the user guessed "p" and the chosen word was "apple", then display
#  should be ["_", "p", "p", "_", "_"].


for letter in range(0, len(chosen_word)):
    if chosen_word[letter] == guess:
        display[letter] = guess  # Using 'letter' as an index


#  Printing 'display' and you should see the guessed letter in the correct
#  position and every other letter replaced with "_".

print(display)

game_over = False
lives = 6

# printing the ASCII art from 'stages' that corresponds to the current number
# of 'lives' the user has remaining.

while game_over is not True:
    # Displaying lives and asking user for a guess
    i = -7 + lives
    print(stages[i])
    print(f"Lives: {lives}")
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
    # Replacing '_' for correct guessers
    for letter in range(0, len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess  # Using 'letter' as an index
    print(display)

    # Defining the 'Game Over'
    if lives == 0:
        game_over = True
        print(stages[0])
        print(f"You Lose! The word is {chosen_word}.")
    if not "_" in display:
        game_over = True
        print("You win!")
    if game_over:
        break
