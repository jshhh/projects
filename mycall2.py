a=0
s=0
n = int(input())
s += 1
if n % 2 == 0:
    a += n
while n!=0:
    n=int(input())
    s+=1
    if n%2==0:
        a+=n
print(s-1)
print(a)