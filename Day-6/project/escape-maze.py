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
    # always move if front is clear
    while (front_is_clear()):
        move()
        turn_left() # check every left if it is clear
        if (front_is_clear()):
            move() # if left is clear, move that direction
        else:
            turn_right() # else turn back right
    # If there is a wall on your right and the front is no longer clear
    if (wall_on_right()):
        turn_left() # turn left
    # If the front is no longer clear but there is no wall on right
    elif (wall_on_right() != True):
        turn_right() # turn right
    else:
        turn_around() # turn around
        move() # move 


# Suggested algorithm: move along with wall on right side, when you are able to move right, move right
while not at_goal():
    # If no wall on right
    if (wall_on_right() != True):
        turn_right() # turn right
        move() # move forward
    # While there is a wall on the right
    while (wall_on_right()):
        # if the front is clear
        if (front_is_clear()):
            move() # move forward
        else:
            turn_left() # if front is not clear and there is a wall on right, move left