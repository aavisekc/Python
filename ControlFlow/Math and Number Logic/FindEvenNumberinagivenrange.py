# Enter two number which will be used for range
# and then print the even numbers in that range
# Author: Aavisek Choudhury
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if (n1%2!=0): # if n1 is odd then add 1 to make it even
    n1+=1
for i in range(n1,n2+1,2):
    print(i,end=" ")