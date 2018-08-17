import random

a = random.randint(1, 100)
b = random.randint(1, 100)


print (a,b)
def nod(a,b):
    while a>0:
        if a<b:
            a,b = b,a
        a=a%b
    return b
x=input('введите первую дробь:')
y=input('введите вторую дробь:')
d=input('введите знак операции:')
x1,x2=x.split('/')
x1=int(x1)
x2=int(x2)
if x2==0:
    print('Error')
    exit(0)
delit1=nod(x1,x2)
x1=x1/delit1
x2=x2/delit1
y1,y2=y.split('/')
y1=int(y1)
y2=int(y2)
if y2==0:
    print('Error')
    exit(0)
delit2=nod(y1,y2)
y1=y1/delit2
y2=y2/delit2

if d=='/':
    y2,y1 = y1,y2

if x2==0 or y2==0:
    print('Error')
    exit(1)

if d in ['*','/']:
    res1=x1*y1
    res2=x2*y2
    if res1==0 and res2!=0:
        print(0)
    else:
        delit=nod(res1,res2)
        res1 = int((x1 * y1)/delit)
        res2 = int((x2 * y2)/delit)
    if res1>=res2:
        print(res1//res2)
        if res1%res2!=0:
            print(res1%res2,'/',res2)
        exit(0)
if x2==0 or y1==0:
    print('Error')
    exit(1)
if d=='+':
    if x2==y2:
        res1=x1+y1
        res2=x2
    else:
        delit=nod(x2,y2)
        if delit==1:
            res1=x1*y2+y1*x2
            res2=x2*y2
        elif x2>y2:
            res1=x1+y1*delit
            res2=x2
        else:
            res1 = x1*delit + y1
            res2 = y2
    delit1=nod(res1,res2)
    res1=int(res1/delit1)
    res2=int(res2/delit1)
if d=='-':
    if x2==y2:
        res1=x1-y1
        res2=x2
    else:
        delit=nod(x2,y2)
        if delit==1:
            res1=x1*y2-y1*x2
            res2=x2*y2
        elif x2>y2:
            res1=x1-y1*delit
            res2=x2
        else:
            res1 = x1*delit - y1
            res2 = y2
    delit1=nod(res1,res2)
    res1=int(res1/delit1)
    res2=int(res2/delit1)




print(res1,'/',res2)
