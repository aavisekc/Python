# Multiplication Table
# This program prints the multiplication table of a given number
# up to 10
# The program prompts the user to enter a number and then prints the multiplication table for that number.
# Author: Aavisek Choudhury
print("Take a number as input and print its multiplication table")
num=int(input("Enter the number: "))
for i in range(1,11):
    Table=num*i
    print(Table)
print("Multiplication table of",num,"is")
for i in range(1,11):
    print(num,"*",i,"=",num*i)
