#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random

print(logo)
# Allow the player to submit a guess for a number between 1 and 100.

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
output = random.randint(1,100)

def guess_num(count):
  while count > 0:
    print(f"You have {count} attempts remaining to guess the number.")
    guess = int(input("make a guess: "))
    if guess == output:
      print(f"You got it! The answer was {output}.")
      count = 0
    elif guess > output:
      print("Too High!.\nGuess Again.")
      count -= 1
      if count == 0:
        print("You've run out of guesses, you lose.")
      #print(f"You have {count} attempts remaining to guess the number")
    elif guess < output:
      print("Too Low!.\nGuess Again.")
      count -= 1
      #print(f"You have {count} attempts remaining to guess the number")
      if count == 0:
        print("You've run out of guesses, you lose.")


if difficulty == "easy":
  count = 10
  guess_num(count)
elif difficulty == "hard":
  count = 5
  guess_num(count)



# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

