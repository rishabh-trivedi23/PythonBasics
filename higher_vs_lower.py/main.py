from art import logo, vs
from game_data import data
import random
from replit import clear
first_draw = random.sample(data,1)
option_a = first_draw[0]
game_on =True
final_score = 0
while game_on:
  second_draw = random.sample(data,1)
  option_b = second_draw[0]
  print(logo)
  print(f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}." )
  
  print(vs)
  print(f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}." )
  option = input("Who has more followers? Type 'A' or 'B': ").lower()
  if option == "a":
    if option_a["follower_count"] > option_b["follower_count"]:
      option_a = option_b
      final_score += 1
      print(f"You are right! Curent Score: {final_score}.")
      clear()
    else:
      print(f"Sorry, that's wrong. Final score: {final_score}")
      game_on = False
  elif option == "b":
    if option_a["follower_count"] < option_b["follower_count"]:
      option_a = option_b
      final_score += 1
      print(f"You are right! Curent Score: {final_score}.")
      clear()
    else:
      print(f"Sorry, that's wrong. Final score: {final_score}")
      game_on = False

