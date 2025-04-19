# Take n numbers as input and compute their average using a for loop.
# The program should ask the user how many numbers they want to enter, and then prompt them to enter each number one by one.
# Finally, it should calculate and display the average of those numbers.
# Author: Aavisek Choudhury
num=int(input("How many numbers do you want to enter? "))
sum=0
for i in range(num):
    n=int(input("Enter number: "))
    sum+=n
average=sum/num 
print("The average of the numbers is: ",average)

