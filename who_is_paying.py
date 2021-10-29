import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇

names_len = len(names)
num = random.randint(0,names_len-1)
print(f"{names[num]} is going to buy the meal today!")