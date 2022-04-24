# Day 21 - Practicing slicing in Python

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
 
print(piano_keys[2:5]) # Output: ["c", "d", "e"]
print(piano_keys[:5]) # Output: ["a", "b", "c", "d", "e"]
print(piano_keys[2:5:2]) # Output: ["c", "e"] (increment by 2)
print(piano_keys[::2]) # Output: ["a", "c", "e", "g"] (increment by 2 from beginning to end)
print([piano_keys[::-1]]) # Output: ["g", "f", "e", "d", "c", "d", "a"]  (reverse list)
