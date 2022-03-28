num=int(input("put your number here:"))
first=num//10
second=num%10

if 10<=num<=99:
    if num%7==0 or first==7 or second==7:
        print("lucky number")
    else:
        print("this isnt a lucky number")
else:
    print("error")



