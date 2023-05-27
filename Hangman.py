import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [ "aardvark",  "baboon", "camel"]
# chosing random word from the list
chosen_word = random.choice(word_list)
print ( f" The chosen word is {chosen_word} ")
# creating an empty list, for adding elements into the list later on.
display = []
# adding '_' no. of time the length in list
for letter in range (len(chosen_word)):
    display+='_'
# printing the result    
print (display)  
'''
def forward():
    for l in range(6):
        print(stages[-position])
'''





  

# creating a function
def fun():
  guess = input (" Enter a letter to guess : ")
  if guess in chosen_word:
    print( f" {guess} IS present in {chosen_word} ")
  else:
    print( f" {guess} IS NOT present in {chosen_word} ")
# This for runs to replace guess with letters
  for position in range(len(chosen_word)):
    letter = chosen_word[position]    
    if letter == guess:
      display[position]=letter
    #  print( stages[-position])
  #  print( stages[position])
  print ( display)        
# creating chose list to add elements of string chosen_word to compare
chose = []
for st in range(len(chosen_word)):
    chose += chosen_word[st]
# running loop and guessing letters until letters become equal to word
for i in range(6):
    while(chose!=display):    
       fun()

# displaying if the player has won or not
if chose==display:
    print ( "\n Lists are similar. You've Won!!! ")
else :
    print (  "\n They aren't. You Lost!!!")




















    