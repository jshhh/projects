from random import randint
s=int(input())
m=[]

bukaffki = []

for i in range(10):
    bukaffki.append(str(i))

for i in range(10,36):
    bukaffki.append(chr(ord('a')+i-10))

print(bukaffki)

a=(randint(16,16))
print(a)
while s!=0:
    m.append(bukaffki[s%a])
    s=s//a
m1=m[::-1]
print(m1)
