# Day 6 Project - Escaping the Maze
#
# Using premade functions, try to escape the maze!
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Turn Right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Turn Around
def turn_around():
    turn_left()
    turn_left()

# Loop through logic till you are at the flag and have escaped the maze
while not at_goal():
    
    while (front_is_clear()):
        move()
        turn_left()
        if (front_is_clear()):
            move()
        else:
            turn_right()
    if (wall_on_right()):
        turn_left()
    elif (wall_on_right() != True):
        turn_right()
    else:
        turn_around()
        move()