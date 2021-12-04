# sum of odd numbers from 1 to n
#n=int(input("Enter the number up to which to find the oddsum:"))
#oddtotal=0
#for number in range(1,n+1):
#    if(number % 2 !=0):
#        print("{0}".format(number))
#        oddtotal=oddtotal+number
#print("The sum of odd numbers from 1 to {0}={1}".format(number,oddtotal))

inp1=range(1,10,2)
sum2=sum(inp1)
print(f"the sum of odd numbers of first ten integer is {sum2}")