#YOu live 4 miles from university. The bus drives at 25 mph but spends 2 minutes at each of the 10 stops on the way.
#HOw long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph;  
#then run the next two at 15mph; beforejogging the last at 7mph again Will this be quicker or slower than the bus?

#bus stops at 10 places and spent 2 minutes
stopTime=10*2
#time covered by bus in 4 miles with 25mph
bustime=((4/25)*60)
totalBusTime=bustime+stopTime
print(f"The total time to reach university by bus is {totalBusTime}")

#jogging with 7mph at 1mile, 15mph at 2mile and 7mph at 1mile

time1=((1/7)*60)
time2=((2/15)*60)
time3=((1/7)*60)
totalJoggingTime=time1+time2+time3
print(f"the total time for walking is{totalJoggingTime}")

if totalJoggingTime>totalBusTime:
    print(f"walking is fast to reach the univerity")
else:
    print(f"going by bus is fast to reach the university")