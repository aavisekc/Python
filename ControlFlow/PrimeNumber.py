# Check if the number is a prime number or not
# Check the edge cases
# Author: Aavisek Choudhury
import math
num=int(input("Enter the number:"))
# Handle the edge cases first
def is_prime(n):
    # If n <= 1: Not prime.
    if (num<=1):
        return False
    # If n == 2: Prime.
    if (num==2):
        return True
    # If n is even and greater than 2: Not prime.
    if(num%2==0):
        return False
    
#So now:
# All even numbers are handled.
# No need to check them again.
# So you start from 3 and only check odd numbers (3, 5, 7, 9, 11, ... √n).
# Loop through odd numbers from 3 to √n (square root of n)+1
# If n is divisible by any of these numbers → Not prime.
# If none divide n evenly → Prime.

    for i in range (3,int(math.sqrt(n))+1,2):
        if (i%2==0):
            return False
    return True
result=is_prime(num)
# Check if the number is prime or not
if result:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")