#Give a n-digit number. Find the sum of its digit.

n=int(input("Enter the n-digit number:"))
sum=0
while n>0:
       remainder=n%10
       sum =sum +remainder
       n=n//10
print(f"the sum of n-digit number is:{sum}")