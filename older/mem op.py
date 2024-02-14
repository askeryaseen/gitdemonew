# a="hello"
# print("e" in a)
# print("z" not in a)

# a=10
# b=10

# print(a is b)
# print(id(a))
# print(id(b))
# print(b is a)

# a=10
# b=20
# c=30
# if a>b and a>c:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# else:
#     print("c is greater")
    
# a=int(input("enter a number \n"))
# if(a%2==0):
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")
    
a=int(input("enter a number \n"))
if (a%2==0):
    print(f"{a} is visible by 2")
    if(a%5==0):
        print(f"{a} is divisible by 5")
    else:
        print(f"{a}is not divisible by 5")
else:
        print(f"{a}is not divisible by 2")