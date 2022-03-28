from random import randint
num1=int(input("choose a number between 0-100:"))
while num1<0 or num1>100:
    print("invalid number")
    num1 = int(input("choose a number between 0-100:"))
num2=randint(1,100)
while num1!=num2:
    while num2>num1:
        num2=randint(1,num2)
    while num2<num1:
        num2=randint(num2,100)
print(f"the correct number is {num2}")





