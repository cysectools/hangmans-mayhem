# __READ PLEASE__ #
# __Hangman Functionality Is Not My Original Work. I Simpy Added More "Fun" To It__ #
# __Hangman Functionality Creator__ [https://www.youtube.com/@ShaunHalverson]
# __Funware Portion Creator__ [@cysectools] / [https://cysectools.com] #
# __ENJOY!__  :) #
# __END READ__ #


import random
import time
import webbrowser
import rotatescreen as rs

print(r"""
# __READ PLEASE__ #
# __Hangman Functionality Is Not My Original Work. I Simpy Added More "Fun" To It__ #
# __Hangman Functionality Creator__ [https://www.youtube.com/@ShaunHalverson]
# __Funware Portion Creator__ [@cysectools] / [https://cysectools.com] #
# __ENJOY!__  :) #
# __END READ__ #""")

print(r"""
   ________  _______ ______________________  ____  __   _____
  / ____/\ \/ / ___// ____/ ____/_  __/ __ \/ __ \/ /  / ___/
 / /      \  /\__ \/ __/ / /     / / / / / / / / / /   \__ \ 
/ /___    / /___/ / /___/ /___  / / / /_/ / /_/ / /______/ / 
\____/   /_//____/_____/\____/ /_/  \____/\____/_____/____/""")
print("\n")

# Infinite Rick-Roll function
def tab_loop():
    url = "https://youtu.be/dQw4w9WgXcQ?si=UNwoed8ATJeaSH9W"
    num_tabs = 2 # Any number greater than 0 (It'll loop regardless)

    for i in range(num_tabs):
        webbrowser.open(url)

print("Welcome to hangman")
print("_ " * 13)

wordDictionary = ["blueteam", "redteam", "cybersecurity", "hacker"]
### Choose a random word
randomWord = random.choice(wordDictionary)
# print(randomWord)

for x in randomWord:
  print("_", end=" ")

def print_hangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1):
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/| |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/| |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|  |")
    print("/   |")
    print("    ===")
    pd = rs.get_primary_display()
    sd = rs.get_secondary_displays()
    angle_list = [0, 90, 180, 270]
    for i in range(5):
        for x in angle_list:
            pd.rotate_to(x)
            time.sleep(0.5)
            tab_loop()
def printWord(guessedLetters):
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
        timer = -10
        while timer < 0:
            time.sleep(0)
            timer = timer + 1

        print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
  ### Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  ### User is right
  if(randomWord[current_guess_index] == letterGuessed):
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  ### User was wrong af
  else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(letterGuessed)
    ### Update the drawing
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()

print("\nGame is over! Thank you for playing :)")