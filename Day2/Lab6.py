#YOu live 4 miles from university. The bus drives at 25 mph but spends 2 minutes at each of the 10 stops on the way.
#HOw long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph; then run the next two at 15mph; before 
#jogging the last at 7mph againl Will this be quicker or slower than the bus?

distance=4
a=25

#bus stops at 10 places and spent 2 minutes
stopTime=10*2
x=1/a
t=x*60
totalTime=t+stopTime
print(f"The total time to reach university by bus is {totalTime}")

#run with the speed of 7 mph
b=7mph
f=1/b
time_1=f*60
c=15
g=1/c
time_2=g*60
d=7
h=1/d
time_3=h*60
total_time2=time_1+time_2+time_3
print(f"the total time for walking is{total_time2})

if total_time2>totalTime:
print(f"walking is fast to reach the univerity")