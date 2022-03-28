num=int(input("put your age here:"))
while 0<=num<120:
    if 0<=num<=18:
        print("child")
    if 19<=num<=60:
        print("adult")
    if 61<=num<=120:
        print("senior")
    num = int(input("put your age here:"))
else:
    print("error")
