# Write a fucntion to find the sum of two numbers
# and return the result
def sum_of_two_numbers(a,b):
    """
    This function takes two numbers as input and returns their sum.
    """
    c=a+b
    # Check if the result is a number
    return c
#take the input from the user
a=int(input("Enter the first number: "))
b=int(input("Enter the second number:"))
# Call the function and print the result
result=sum_of_two_numbers(a,b)
print("The sum of the two numbers is:", result) 
print(f"The sum of {a} and {b} is: {result}")

