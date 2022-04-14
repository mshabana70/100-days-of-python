# Day 12 - Scope (Local - Global)

# Scope
enemies = 1 # Global

def increase_enemies():
    enemies = 2 # Local (can only be referenced in function scope)
    print(f"enemies inside the function: {enemies}") # Output: 2

increase_enemies()
print(f"enemies outside the function: {enemies}") # Output: 1