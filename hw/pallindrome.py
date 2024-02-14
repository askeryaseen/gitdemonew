user = input("enteryour string :?")
reverse = ""
for i in user:
    reverse = i + reverse
print(reverse)
if user == reverse:
     print(user," is a pallindrome")
else:
    print("not a palindrome")