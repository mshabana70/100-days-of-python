# Day 26 Project - NATO alphabet

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd

nato_df = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Please give us a word to translate: ").upper()

result = {nato_dict[letter] for letter in user_word}
print(result)