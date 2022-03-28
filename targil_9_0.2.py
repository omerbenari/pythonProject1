day=int(input("put your day here:"))
month=int(input("put your month here:"))
year=int(input("put your year here:"))
right=year%10
middle=year%100//10
if day<1 or day>31 or month<1 or month>12 or year<1950 or year>2020:
    print("invalid")
if 1<=day<=9:
        print(f"0{day}/{month}/{middle}{right}")
    if 1<=month<=9:
        print(f"{day}/0{month}/{middle}{right}")
        else:
        print(f"{day}/{month}/{middle}{right}")




