#this system will get 2 numbers and print 4 different calculations of them
from random import randint
num1=randint(1,100)
num2=randint(1,100)
print(f"{num1}+{num2}={num1+num2}\n"
      f"{num1}-{num2}={num1-num2}\n"
      f"{num1}*{num2}={num1*num2}\n"
      f"{num1}/{num2}={num1/num2}")
