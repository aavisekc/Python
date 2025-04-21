# Program to draw right angled traingle with star
# A right-angled triangle is a triangle in which one angle is a right angle (90 degrees).
# In this case, the right angle is at the bottom left corner.
# The triangle is formed by printing numbers in a specific pattern.
# Author: Aavisek Choudhury 

rows=input("Enter the number of rows: ")
rows=int(rows)
for i in range(1, rows + 1):
    print("Row number is", i)
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line
# # Output:
# """   
# 1
# 1 2                       

