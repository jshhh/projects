from random import randint
a=[]
n=10
x=0
f=True
while n!=0:
    a.append(randint(1,100))
    n-=1
for i in range(len(a)):
    x+=1
    if not f:
        break
    f = False
    for j in range(len(a)-i-1):
        x+=1
        if a[j]>a[j+1]:
            f = True
            a[j],a[j+1]=a[j+1],a[j]
print(x)
print(a)