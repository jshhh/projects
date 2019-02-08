amount=int(input('vviditi kolidstvo disel'))
c=int(input())
d=0
for i in range(0,amount-1):
    b=int(input())
    if (c>b or c%3!=0) and b%3==0:
        c=b
    if (c>b or c%3!=0) and b%3==0 and b!=c:
        d=b

if c%3!=0:
    c = 1
print(c,d)
