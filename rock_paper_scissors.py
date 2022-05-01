rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
image = [rock,paper,scissors]
b = "yes"

while(b=="yes"):
  a = int(input("Enter your choice 0 for rock 1 for papper 2 for scissors:-"))
  x = random.randint(0,2)

  if a>=3 or a<0:
    print("Invalid Input!!!")

  elif(a==x):
    print(f"you chose:-{image[a]}")
    print(f"computer chose:-{image[x]}")
    print("Game Draw!!!")

  elif(a==0 and x==2):
    print(f"you chose:-{image[a]}")
    print(f"computer chose:-{image[x]}")
    print("You Won!!!")

  elif(a==2 and x==0):
    print(f"you chose:-{image[a]}")
    print(f"computer chose:-{image[x]}")
    print("You lost!!!")  

  elif(a>x):
    print(f"you chose:-{image[a]}")
    print(f"computer chose:-{image[x]}")
    print("You Won!!!")

  elif(a<x):
    print(f"you chose:-{image[a]}")
    print(f"computer chose:-{image[x]}")
    print("You lost!!!")
  
  c=input("Enter yes to play again:-")
  b=c.lower()