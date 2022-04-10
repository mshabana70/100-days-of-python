# Day 8 Project - Caesar Cipher 
#
# Create a caesar cipher program that can encrypt and
# decrypt messages inputed by the user along with a 
# shift number

# Program set up

# letters for our alphabet
letters = "abcdefghijklmnopqrstuvwxyz"
letters_list = list(letters)
print (letters_list)

# User input values
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(message, shift, direction):
    index = 0
    new_message = ""
    message_list = list(message) # set message to a list

    # Iterate through the message_list
    for i in range(len(message_list)):

        # If a letter in message is in the alphabet (so it ignores spaces and symbols)
        if message[i] in letters_list:

            # get index of letter in the letter_list (so we can shift from this point to the new encoded letter)
            index = letters_list.index(message_list[i])

            # check the direction (encode or decode)
            if (direction == 'encode'):

                # If the shift excedes the size of our list, start back at the beginning (loop back to the front)
                if ((index + shift) > (len(letters_list) - 1)):
                    index = (index + shift) - (len(letters_list)) # subtract length from new index to start from beginning
                else: 
                    index += shift
                message_list[i] = letters_list[index] # set message letter to the new encoded letter (post shift)
            else:
                # If the shift excedes the size of our list, start back at the beginning (loop back to the front)
                if ((index - shift) < 0):
                    index = (index - shift) + (len(letters_list)) # add length from new index to start from the end
                else: 
                    index -= shift
                message_list[i] = letters_list[index] # set message letter to the new decoded letter (post shift)
    new_message = new_message.join(message_list) # join message back to a string for readablility
    print(f"The {direction}ed message is {new_message}") # print back new message

caesar_cipher(text, shift, direction)


        

