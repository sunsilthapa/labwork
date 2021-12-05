
#Given the integer N-number of minute that is passed since midnight - how many hours and minutesare displayed 
#on the 24h digital clock? The program should print two numbers: the number of hours (between 0 and 23) and the
#number of minutes (between 0 and 59). For example, if N=150, then 150 minutes have passed since midnight -i.e now
#is 2:30 am. so, the program should print 2:30

NoOfminutes=int(input("Enter the minute since midnight"))
hours=NoOfminutes//60
minutes=NoOfminutes%60
print(f"{hours}:{minutes}")