n=int(input())
a=[]
d=0
for i in range(n):
    f=int(input())
    a.append(f)
a=sorted(a)
for j in range(n-1,0,-1):
    for i in range (j-1,0,-1):
        if a[j]*a[i]%10!=0:
            d=a[j]*a[i]
            print(d)
            exit(0)

print(d)