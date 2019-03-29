from random import randint

# n=int(input('amount: ?'))
names = ('ivan','boris','anton','kirill','alex')
lnames = ('ivanov','petrov','sidorov','kuznetsov','melnikov')
# for i in range(0,n):
#     strng = names[randint(0,4)]+' '+lnames[randint(0,4)]+' 50 '+randint(1,99).__str__()
#     print(strng)
#     info.append(strng.split(' '))


name_num = randint(0,len(names))
lname_num = randint(0,len(lnames))

for i in range(7):
    name_num+=6
    if name_num>len(names)-1:
        lname_num+=1
        lname_num%=len(lnames)
        name_num%=len(names)
    print(names[name_num],lnames[lname_num])

a=[1,2,3,4,5,6,7,8,9,10]
b=[0,0,0,0,0,0,0,0,0,0]

c = [
    (1,0),
    (2,0),
    (3,0),
    (4,0),
    (5,0),
    (6,0),
    (7,0),
    (8,0),
    (9,0),
    (10,0),
]

for i in range(700):
    f=randint(1,10)
    c[f-1][1]+=1
b=sorted(b)
print(b[0])
print(b[9])`