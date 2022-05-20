# Type Hints 
age: int
name: str
height: float
is_human: bool

# Arrow defines the expected datatype of function output
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    # This causes an error due to our arrow definition
    #return "They can drive" 
    return can_drive

# print(police_check(12))
# print(police_check(19))

if police_check(19):
    print("you may pass.")
else:
    print("Pay a fine.")

# This will throw an error since we defined 'age' to be an int in police_check()
# if police_check("twelve"):  
#     print("you may pass.")
# else:
#     print("Pay a fine.")