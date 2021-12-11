#Ask user to enter ae, gender (M or F) and then using followingrules print their place of service.
#if employee is female, thn she will wor only in urban area.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 to 60 then he will in urban areas only.
#And any other input of age should print "ERROR"

age=int(input("Enter your age:"))
gender=str(input("Enter your gender:"))
if gender=='F':
    print("She will work only in urban area")
elif gender=='M' and (age>20 and age<40):
    print("He will work anywhere")
elif gender=='M':
    print("He will work only in urban area")
else:
    print("ERROR")
