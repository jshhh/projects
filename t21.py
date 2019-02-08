n=int(input())
a=int(input())
b=0
c=0
e=0
while e<n-1:
    e+=1
    d=int(input())
    if d>=a:
        a=d
    elif d<=a and d>=b:
        b=d
    elif d<=b and d>=c:
        c=d
print(a,b,c)
