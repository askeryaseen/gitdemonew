s1 = "hen"
s2 = "animal"
s2 = s2[::-1]
# print(s2)
s = " "
l1 = len(s1)
l2 = len(s2)

if l1>l2:
    l = l1
else: 
    l = l2
for i in range(l):
    if i <l1:
        s += s1[i]
    if i<l2:
        s += s2[i]
        
print(s)    