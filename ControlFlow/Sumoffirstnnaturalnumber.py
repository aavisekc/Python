# Sum of first n natural numbers
# This program calculates the sum of the first n natural numbers
# using a for loop.
# It prompts the user to enter a number and then computes the sum.
# Author: Aavisek Choudhury
num=int(input("Enter a number: "))
sum=0
for i in range (0,num+1):
    sum=sum+i
print("The sum of first",num,"natural numbers is",sum)