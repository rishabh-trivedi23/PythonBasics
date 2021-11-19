import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato = {alphabet:phonetic for (alphabet,phonetic) in df.iterrows()}

new_dict = {value['letter']:value['code'] for key, value in nato.items()}

user_input = input("Please enter a word: ").upper()
new_list = [new_dict[items] for items in user_input]

print(new_list)
