#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

def play_game(y):
  global life
  if y == "easy":
    print("You have 10 attempts remaining to guess the number.")
    user_input=int(input("Make a guess:-"))
    for _ in range(9):
      if user_input == x:
        print("You win!!!")
        break;
      elif user_input > x:
        print("Too High!!!")
        user_input=int(input("Guess again:-"))
      elif user_input < x:
        print("Too Low!!!")
        user_input=int(input("Guess again:-"))
        
      life+=1
    return user_input
    
  elif y == "hard":
    print("You have 5 attempts remaining to guess the number.")
    user_input=int(input("Make a guess:-"))
    for _ in range(4):
      if user_input == x:
        print("You win!!!")
        break;
      elif user_input > x:
        print("Too High!!!")
        user_input=int(input("Guess again:-"))
      elif user_input < x:
        print("Too Low!!!")
        user_input=int(input("Guess again:-"))
      
      life+=1
    return user_input
  
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
y = input("Choose a difficulty. Type 'easy' or 'hard':-") 
x = random.randint(1,100)
life = 1

a=play_game(y)
if(a!=x):
  print("You Lose, you run out of lives!!!")