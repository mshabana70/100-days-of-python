# Day 26 Project - NATO alphabet

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd

nato_df = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)
new_result = []

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    # Day 30 coding exercise - Exception Handling of KeyError
    user_word = input("Please give us a word to translate: ").upper()
    try:
        for letter in user_word:
            new_result.append(nato_dict[letter])
        result = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)
        print(new_result)

# Call new function
generate_phonetic()