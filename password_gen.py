import string
import random as r
letters = string.ascii_uppercase + string.ascii_lowercase +string.digits + string.punctuation

print("welcome to Password Generator")
l = int(input("enter length of password: "))

li=[]
for i in range(l+1):
    if l>=8:
        char = r.choice(letters)
        li += char
    else:
        print("Reqiured minimum 8 characters")
        break

r.shuffle(li)
le=""
for i in li:
    le +=i
print(le)

