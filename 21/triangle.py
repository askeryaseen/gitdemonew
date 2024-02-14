side_1 = int(input("enter length of first side "))
side_2 = int(input("enter length of second side "))
side_3 = int(input("enter length of Third side "))

if side_1 == side_2 == side_3:
    print("triangle is equilateral")
elif side_1==side_2 or side_2==side_3 or side_1==side_3:
    print("triangle is isocles")
elif side_1!=side_2!=side_3:
    print("triangle is scalene")
else:
    print("enter sides properly")