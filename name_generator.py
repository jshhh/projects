from random import randint

names = ('ivan','boris','anton','kirill','alex','konstantin')
lnames = ('ivanov','petrov','sidorov','kuznetsov')
n=int(input())
b=[names[randint(0,len(names)-1)],lnames[randint(0,len(lnames)-1)]]
c=0
print(b)
checker = []
while n!=0:
    a=[names[randint(0,len(names)-1)],lnames[randint(0,len(lnames)-1)]]
    if a[0]!=b[0] and a[1]!=b[1]:
        n-=1
        print(a)
        b=a
        c=b
    checker.append(a)
if n==0:
    print('True')


print(sorted(checker))