#Take username and password from user and check it again for the three times whether the user has entered the right
#username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".

username=input("Enter your username")
userpassword=input("Enter your password")
for i in range(0,3):
    print("Enter your credentials")
    username1=input("Enter your username:")
    password2=input("Enter your password:")
    if username==username1 and password==password1:
        print("You are successfully logged")
        break
    elif i<3:
        if(username!=username1 or password1!=password1):
            print("Invalid Credentials")
else:
    print("3 attempt finished")