# N students take K apples and distributed them among each other evenly. The remaining (the indivisible) part remain
#in the basket. How manay apples will each single student get? How many apples will remain in the basket? The program reads the numbers N 
#and K. It should print the two answers for the questions above. A school decided to repllace the desks in three classrooms. Eaach deskssits two students. Given 
#the number of students in each class, print the smallest possible number of desks that can be purchased.

stdno=int(input("Enter the no of students:"))
apple=int(input("Enter the no of apples:))
a=apple//stdno
b=apple%stdno
print(f"The number of apple each student will get: {a}")
print(f"The number of apple each student will get: {b}")
