s1 ="hey"
s2="hellomacha"

s3 = s2[::-1]

l1 = len(s1)
print(l1)
l2 = len(s2)
print(l2)

if l1>l2:
    l = l1-l2
    print(l)
else:
    l = l2-l1
    print(l)
s= " "
for i in range(l):
    if i<l:
        s +=s1[i]
    
    s +=s2[i]
    
print(s)
