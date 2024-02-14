limit = int(input("enter limit"))
a = 0
b = 1
n = 0
while n<limit:
    c = a + b
    a = b
    b = c
    n+=1
    print(c)