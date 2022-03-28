from random import randint
num=randint(1,9)
num1=int(input("guess the number"))
while num!=num1:
        if num1>num:
            print("higher than the number")
            num1 = int(input("guess the number"))
        else:
            print("lower than the number")
            num1 = int(input("guess the number"))
print("the correct answer")

