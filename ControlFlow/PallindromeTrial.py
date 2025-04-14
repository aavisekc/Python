
# Palindrome function to check if a number is a palindrome or not

def checkPallindrome(number):
    original_number = number
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10
    
    if original_number == reverse_number:
        return True
    else: 
        return False

    # Call the function

number = int(input("Enter a number: "))
if checkPallindrome(number):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome") 

# End of code