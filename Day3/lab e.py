#Given three integers, print the smallest one.
#(Three integers should be user input)

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a<b and a<c:
    print(f"a is the smalles one")
elif b<a and b<c:
    print(f"b is the smallest one")
else:
    print(f"c is the smallest one")