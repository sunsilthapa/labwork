#WAP which accepts marks of four subjects and display total marks,
#percentage and grade. Hint: more than 70% then distinction, more 
#than 60% then first, more than 40% then pass, less than 40% then fail.

a=int(input("Enter the mark of science:"))
d=int(input("Enter the mark of social:"))
b=int(input("Enter the mark of math:"))
c=a+b+d
e=(c/400)*100
print(f"The total percentage is {e}")
if e>70 and e<100:
   print("you scored distinction")
elif e>60 and e<=70:
   print("you scored first grade" )
elif e>40 and e<=60:
    print("you are pass")
else:
    print("you are fail")