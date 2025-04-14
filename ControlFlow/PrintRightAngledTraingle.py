"""
*
**
***
****
*****
"""
# Explaination
""" 
range(1, 6)
This means the loop variable i will go from 1 to 5 (not including 6):
So, i takes values: 1, 2, 3, 4, 5
print("*" * i)
This multiplies the * character i times. For example:
When i = 1, it prints: *
When i = 2, it prints: **
When i = 3, it prints: ***
And so on...
Why it forms a triangle?
Each line has one more * than the previous, forming a growing right-angled triangle along the left side. 
"""
# Program to draw right angled traingle with star
# A right-angled triangle is a triangle in which one angle is a right angle (90 degrees).
# In this case, the right angle is at the bottom left corner.
# The triangle is formed by printing '*' characters in a specific pattern.
# Author: Aavisek Choudhury 

for i in range(1, 11):
    print("*" * i)  # Print '*' i times, where i is the current line number