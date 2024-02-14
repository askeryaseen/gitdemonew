b ='malayalam'
z='recover'
for i in z:
    c = 0
    for j in z:
        if i==j:
            c+=1
    if c==1:
        print(i)
        