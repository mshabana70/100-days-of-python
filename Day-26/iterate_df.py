# Iterate Dataframes like we do for dictionaries

import pandas as pd

student_dict = {
    "student": ["Mahmoud", "Angela", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# # Loop through a dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #print(row.student)
    #print(row.score)
    if row.student == "Mahmoud":
        print(row.score)
