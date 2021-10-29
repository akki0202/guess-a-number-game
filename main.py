#Number Guessing Game Objectives:
import art
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
number=random.randrange(1,100)
print(art.logo)
print("Wellcome to number guessing game!")
print("I'm thinking of a number.")
level=input("Would you like to play 'easy' or 'hard'? ")
if level=='hard':
  a=5
  while a != 0:
    print(f"You have {a} attempts to guess. ")
    guess=int(input("make a guess: "))
    if guess == number:
      a=0
      print("You win!")
    elif guess>number:
      a-=1
      if a==0 and guess != number:
          print("You lose.")
      else:
          print("too high \nguess again.")
    elif guess<number:
      a-=1
      if a==0 and guess != number:
          print("You lose.")
      else:   
          print("too low \nguess again.") 
       
elif level=='easy':
  a=10
  while a != 0:
    print(f"You have {a} attempts to guess. ")
    guess=int(input("make a guess: "))
    if guess == number:
      a=0
      print("You win!")
    elif guess>number:
      a-=1
      if a==0 and guess != number:
          print("You lose.")
      else:
          print("too high \nguess again.")
    elif guess<number:
      a-=1
      if a==0 and guess != number:
          print("You lose.")
      else:   
          print("too low \nguess again.") 