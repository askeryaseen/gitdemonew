number=int(input("enter number"))
count = 0
sum =0
sum_1 = 0
while number>0:
    mod= number%10
    number = number//10
    
    # count+=1
    sum= sum+mod
print(count) 
print(sum)