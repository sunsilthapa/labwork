#Check whether the user input number is even or odd and 
#display it to user.

a=int(input("Enter the number:"))
if a%2==0:
    print(f"Entered number is even: {a}")
else:
    print(f"Entered number is odd: {a}")