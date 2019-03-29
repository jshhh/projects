from random import randint

a=[0,0,0,0,0]
n=int(input())
while n!=0:
    # b=int(input())
    b=randint(1,5)
    a[b-1]=a[b-1]+1
    n-=1
print(a)
aa=sorted(a)
print(aa[4],aa[3],aa[2])
print(a.index(aa[4])+1,a.index(aa[3])+1,a.index(aa[2])+1,)
