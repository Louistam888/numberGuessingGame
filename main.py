#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import os 
import random 
from art import logo 
print(logo)

guesses = 0 

def startGame():

  number = random.randint(1, 100)
  def clear_screen():
    # Clears screen
    os.system('cls' if os.name == 'nt' else 'clear')


  def restartGame():
    restart = input("Do you want to play again? Type Y for yes and N for no. ").lower()

    if restart == "y":
      clear_screen()
      startGame()
    elif restart == "n":
      print("Thanks for playing!")
    else: 
      restartGame()


  # GAME START
  print("Welcome to the Number Guessing Game")
  print("I'm thinking of a number between 1 and 100")


  def chooseDifficulty():
    global guesses 
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard.' ").lower()

    if difficulty == "easy":
      guesses += 10
      
    elif difficulty == "hard":
      guesses += 5
    
    else: 
      print("This is not a difficulty level. Try again.")
      chooseDifficulty()
  

  def startGuessing():
    global guesses
    
    if guesses == 0: 
      print("You are out of guesses. You lose.")
      restartGame() 

    userPick = int(input("Guess a number between 1 and 100 "))
    
    if userPick == number:
      print(f"Congratulations! You guessed correctly! The number was {number}")
      restartGame()
    
    elif userPick != number: 
      guesses = guesses - 1
      print(f"That's not the number.")

      if guesses > 0:
        print(f"You have {guesses} guesses left.")
        startGuessing()

      elif guesses == 0:
        print("You are out of guesses.")
        restartGame()

  chooseDifficulty()
  startGuessing() 
startGame()