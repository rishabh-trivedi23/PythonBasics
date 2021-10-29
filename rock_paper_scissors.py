import random
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

#Write your code below this line 👇

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input == 0:
  print(rock)
elif user_input == 1:
  print(paper)
elif user_input == 2:
  print(scissors)
comp_input = random.randint(0,2)
print(f"computer chose: {comp_input}")
if comp_input == 0:
  print(rock)
elif comp_input == 1:
  print(paper)
elif comp_input == 2:
  print(scissors)
if user_input == comp_input:
  print("The match is drawn")
elif (user_input == 0 and comp_input != 1) :
  print("You Won!")
elif user_input == 1 and comp_input != 2:
  print("You Won!")
elif user_input == 2 and comp_input != 0:
  print("You Won!")
else:
  print("You Lost!")