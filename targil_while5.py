num=int(input("enter number here:"))
first = num // 10
second = num % 10
while 10<=num<=99:
    first = num // 10
    second = num % 10
    if num%7==0 or first==7 or second==7:
        print("lucky number!")
        num = int(input("enter number here:"))
    else:
        print("unlucky number")
        num = int(input("enter number here:"))