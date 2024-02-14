start = int(input("enter starting number ?"))
stop = int(input("enter stoping number ? "))
for i in range(start,stop):
    for j in range(2,i):
        if i%j == 0:
            print(i,"is not prime")
            break
    
    else:
        print(i,"its a prime")