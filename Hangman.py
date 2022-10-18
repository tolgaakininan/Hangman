import random as rand
import os
import time
def printHangMan(lives):
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
    print(stages[lives])
word_list=["elma","armut","maymun","araba","kelime","evrim","ağaç","matematik","algoritma"]

secretWord=rand.choice(word_list)
lives=6
game_is_finished=False
display=[]
for i in range(len(secretWord)):
    display.append("*")
while not game_is_finished:
  
    
    printHangMan(lives)
    print(display)
    guess=input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(0,len(secretWord) ):
        letter=secretWord[position]
        if guess==letter:
            display[position]=letter
    
    if guess not in secretWord:
        print(f"you've guessed {guess} but unfortunately it is not in the word, you lost a life")
        lives-=1        
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    if not "*" in display:
        game_is_finished = True
        print("You win.")
