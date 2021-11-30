# sum of odd numbers from 1 to n
n=int(input("Enter the number up to which to find the sum:"))
oddtotal=0
for number in range(1,n+1):
    if(number % 2 !=0):
        print("{0}".format(number))
        oddtotal=oddtotal+number
print("The sum of odd numbers from 1 to {0}={1}".format(number,oddtotal))