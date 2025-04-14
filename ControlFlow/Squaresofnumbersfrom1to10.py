# Print the squares of numbers from 1 to N
# This program takes an integer input N and prints the squares of all integers from 1 to N.
# Author: Aavisek Choudhury
#Print Squares of Numbers from 1 to N
n=int(input("Print enter the number:"))
for i in range (1,n+1):
  print("Square of",i,"is",i*i)

#Print Squares of Numbers from 1 to N in another way

n = int(input("Enter another number: "))
for i in range(1, n + 1):
    print(f"Square of {i} is {i ** 2}")
    