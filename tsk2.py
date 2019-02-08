from random import *

mylist = []
for i in range(100):
    mylist.append(randint(1,100))

mylist = sorted(mylist)
a=randint(1,100)
print(a)
for i in range(len(mylist)):
    print(i,mylist[i])
for i in range(len(mylist)):
    if a==mylist[i]:
        print(i,a)


