# A student will not be allowed to sit in exam if his/her attendence is
#less than 75%. Take following input from user
#Number of classes held
#Number of classes attended.
#and print percentage of class attended
#is student is allowed to sit in exam or not.

a=int(input("Enter the no of class held"))
b=int(input("Enter the no of classes attended"))

percentage=(b/a)*100
if percentage>=75:
    print(f"You are allowed to sit in the exam")
elif percentage<75:
    print(f"You are not allowed to attend exam")