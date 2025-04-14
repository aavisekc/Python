# Program to write a function to find whether the number is even or odd
# Author: Aavisek Choudhury
def find_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Test the function

number = int(input("Enter a number: "))
result= find_even_odd(number)
print(f"The number {number} is {result}.")