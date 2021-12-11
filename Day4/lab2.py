#Write a python program to sum three given integer. 
#However, if two or more values are equal sum will be zero

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
sum=a+b+c
if a!=b and a!=c:
    print(f"the sum is: {sum}")
else:
    print(f"the sum will ber zero")