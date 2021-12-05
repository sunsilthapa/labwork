# N students take K apples and distributed them among each other evenly. The remaining (the indivisible) part remain
#in the basket. How manay apples will each single student get? How many apples will remain in the basket? The program 
# reads the numbers N and K. It should print the two answers for the questions above.

stdno=int(input("Enter the no of students:"))
apple=int(input("Enter the no of apples:"))
a=apple//stdno
b=apple%stdno
print(f"The number of apple each student will get: {a}")
print(f"The number of apple remaining in the basket: {b}")
