day=int(input("put your day here:"))
month=int(input("put your month here:"))
year=int(input("put your year here:"))
right=year%10
middle=year%100//10
if 1<=day<=31 and 1<=month<=12 and 1950<=year<=2020:
    print(f"{day}/{month}/{middle}{right}")
else:
    print("invalid")