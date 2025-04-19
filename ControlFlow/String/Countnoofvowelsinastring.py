# Count the number of vowels in a string
# This program counts the number of vowels in a given string
# and prints the result.
# Author: Aavisek Choudhury
vowels="aeiouAEIOU"
str=input("Enter the string: ")
count=0
for chr in str:
 if chr in vowels:
     count+=1
print("The number of Vowels in the string is", count)