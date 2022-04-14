# Day 12 - Scope (Local - Global)

# Scope
enemies = 1 # Global

def increase_enemies():
    enemies = 2 # Local (can only be referenced in function scope)
    print(f"enemies inside the function: {enemies}") # Output: 2

increase_enemies()
print(f"enemies outside the function: {enemies}") # Output: 1


# How to modify a global scope

new_enemies = 1

def increase_enemy():
    global new_enemies # takes global variable and allows us to modify it
    new_enemies += 1
    print(f"enemies inside the function: {new_enemies}")

increase_enemy()
print(f"enemies outside the function: {new_enemies}")

# NOTE: It is not recommened to modify global scope

# Constants and Global Scope

PI = 3.14159265 # Global constants are values you define and never plan to modify
# Naming convention for global constants is all UPPERCASE
