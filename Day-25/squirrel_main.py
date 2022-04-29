# Day 25 - Squirrel Data Analysis with Pandas
#
# Challenge: Find the count of each type of fur color 
# in our squirrel census data

import pandas as pd

squirrel_data = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_fur = squirrel_data["Primary Fur Color"]

# Grey Squirrels
grey_squirrels = squirrel_data[squirrel_fur == "Gray"]
grey_squirrels_count = len(grey_squirrels)

# Red Squirrels
red_squirrels = squirrel_data[squirrel_fur == "Cinnamon"]
red_squirrels_count = len(red_squirrels)

# Black Squirrels
black_squirrels = squirrel_data[squirrel_fur == "Black"]
black_squirrels_count = len(black_squirrels)

# Place count and fur color in a dataframe (dict => dataframe)
squirrels_count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Fur Color Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

squirrels_count_df = pd.DataFrame(squirrels_count_dict)

# Read dataframe to csv (squirrel_count.csv)
squirrels_count_df.to_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/squirrel_count.csv")


