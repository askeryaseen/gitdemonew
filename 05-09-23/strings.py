s1="abcde"
s2="uvwxyz"
cs = s1[0]+s2[0]
print(len(s1))
length = len(s1)
middle = length//2

middle_alpha = s1[middle]
print(middle_alpha)

length = len(s2)
middle_2 = length//2

middle_alpha_2 = s2[middle_2]
print(middle_alpha_2)
cs2 = s1[-1]+s2[-1]

cs = cs +middle_alpha+middle_alpha_2+cs2
print(cs)