#the system will get a 3 digit number and will print the biggest digit of them
num=int(input("put your 3 digit number here:"))
num1=num//100
num2=num%10
num3=num//10%10
if num1>num2 and num1>num3:
    print(num1)
if num2>num1 and num2>num3:
    print(num2)
if num3>num1 and num3>num2:
    print(num3)