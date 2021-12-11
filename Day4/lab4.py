#Write a program to print absolute value of a number entered by user.
#eg. input: 1  output:1
#     input:-1 output:1

num=int(input("Enter a number:"))
if num<=0:
    print(f"Your absolute value is",-num)
else:
    print(f"Your absolute value is",num)

