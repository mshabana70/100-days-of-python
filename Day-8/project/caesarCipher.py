# Day 8 Project - Caesar Cipher 
#
# Create a caesar cipher program that can encrypt and
# decrypt messages inputed by the user along with a 
# shift number

# Program set up
import caesarArt

# letters for our alphabet
letters = "abcdefghijklmnopqrstuvwxyz"
letters_list = list(letters)
#print (letters_list)

# User input values
# print(caesarArt.logo, "\n")
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

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

#caesar_cipher(text, shift, direction)


# Angela's Solution

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = letters_list.index(letter)
        new_position = position + shift_amount
        new_letter = letters_list[new_position % (len(letters_list))]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

#encrypt(plain_text = text, shift_amount = shift)

# Create a function called 'decrypt'
def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = letters_list.index(letter)
        new_position = position - shift_amount
        new_letter = letters_list[new_position % (len(letters_list))]
        cipher_text += new_letter
    print(f"The decoded text is {cipher_text}")

# decrypt(plain_text = text, shift_amount = shift)

# Create a function called "caesar()" that puts encrypt and decrypt together

def caesar(plain_text, shift_amount, direction):
    cipher_text = ""
    for letter in plain_text:
        if letter in letters_list:
            position = letters_list.index(letter)
            if direction == "encode":
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount
            new_letter = letters_list[new_position % (len(letters_list))]
        else:
            new_letter = letter
        cipher_text += new_letter
    print(f"The {direction}d text is {cipher_text}")

end_program = False
print(caesarArt.logo, "\n")
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text = text, shift_amount = shift, direction = direction)
    switch = input("Do you wish to rerun the cipher? Yes or No?")
    if switch.lower() == "yes":
        end_program = True
        print("Thank you for using Caesar Cipher!")