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
    message_list = list(message)
    for i in range(len(message_list)):
        if message[i] in letters_list:
            index = letters_list.index(message_list[i])
            if (direction == 'encode'):
                if ((index + shift) > 25):
                    index = (index + shift) - 26
                else: 
                    index += shift
                message_list[i] = letters_list[index]
            else:
                if ((index - shift) < 0):
                    index = (index - shift) + 26
                else: 
                    index -= shift
                message_list[i] = letters_list[index]
    new_message = new_message.join(message_list)
    print(f"The {direction}ed message is {new_message}")

caesar_cipher(text, shift, direction)


        

