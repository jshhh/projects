from random import randint
aa=[]
a=randint(10,20)
for i in range(0,a):
    f=randint(-1000,1000)
    aa.append(f)
#     10 1 5 7 8

b=aa[0]
c=aa[1]
d=aa[2]
b,c,d = sorted((b,c,d),reverse=True)
print(b)
print(c)
print(d)

for j in range(3,a):
    if b<aa[j]:
        d = c
        c = b
        b=aa[j]
    elif c<aa[j]:
        d=c
        c = aa[j]
    elif d<aa[j]:
        d=aa[j]


print(aa)
print(sorted(aa))
print(b)
print(c)

