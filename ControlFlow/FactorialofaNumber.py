# Write a program to find the factorial of a number.
# The factorial of a number n is the product of all positive integers less than or equal to n.  
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
# The factorial of 0 is defined to be 1.
# The factorial of a negative number is undefined.
# The factorial of a number n is denoted by n!.
# The factorial of a number n can be calculated using the following formula:
# n! = n * (n - 1)!
# Factorial of a number
# Author : Aavisek Choudhury
num=int(input(" Enter the number:"))
i=0
fact=1
for i in range (num,i,-1):
   fact=i*fact
print("The factorial of",num,"is",fact)
