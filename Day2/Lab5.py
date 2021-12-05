#A school decided t replace the desks in three classrooms. Each desk sits two students. 
#Given the number of students in each class, print the smallest possible number of desks that an be purchased. 
#The program shuld read three integers. the number of students in each of the three classes, a , b and c respectively
#Suppose in the first test there are three groups. the afirst group has 20 students and thus needs 10 desks.
#The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group
#group of 22 students. So, we need 32 desks in total.

a=int(input("Enter the no student in first class:"))
b=int(input("Enter the no student in second class:"))
c=int(input("Enter the no student in third class:"))
sum=a//2+b//2+c//2+a*2+b%2+c%2
print(f"The total no of desks we needed is {sum}")