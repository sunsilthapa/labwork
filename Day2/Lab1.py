#sec=86400
#day=sec/86400
#hour=sec/3600
#minute=sec/60
#print("in day ")

s=int(input("enter the value for second"))
Day=(((s/60)/60)/24)
print(f"total day for give second :{Day}")
Hour=((s/60)/60)
print(f"total hours for given seconds: {Hour}")
Minute=(s/60)
print(f"the minutes for given second:{Minute}")

