# This program counts the number of characters in a string
# using a for loop
# Author: Aavisek Choudhury
str = input("Enter the string: ")
count = 0
for char in str:
    # Don't count if there is a space in the string
    # or if the character is a space
    if char != ' ':
        count += 1

print("The number of charecters in the string is:",count)