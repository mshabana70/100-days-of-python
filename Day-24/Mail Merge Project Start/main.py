#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
    

# Start of project 

# Get the names from invited_names file
with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-24/Mail Merge Project Start/Input/Names/invited_names.txt") as data:
    names = data.readlines()

# Read the format of the letter template
with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

    # For each name in our list of invited names
    for name in names:

        # Strip the '\n' tag on our name
        clean_name = name.strip()

        # Replace the '[name]' string in our letter template with the desired name
        new_letter = letter_content.replace("[name]", clean_name)

        # Create a new file to be placed in ReadyToSend Dir.
        with open(f"/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-24/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name}.txt", mode = 'w') as data:

            # Write the new letter contents to the new file
            data.write(new_letter)

    