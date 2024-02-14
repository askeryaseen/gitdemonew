number = int(input("enter any number  "))
number_1 = number
count = 0 
sum = 0
while number>0:
    mod = (number%10)**3
    number = number//10
    sum = sum + mod
    count+=1
if number_1 == sum:
    print(f"{number_1} is an amstrong number")
    
print(count) 
# print(sum)