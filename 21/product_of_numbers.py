start =int(input("starting number"))
stop=int(input("stopping number"))
product = 1
while(start<stop):
    product = start * product
    
    start+=1
    print(product)