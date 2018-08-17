koefs=input('input coeffs')

def polyprep(koefs):
    for i in range(len(koefs)):
        koefs[i] = int(koefs[i])
    return koefs

c=[]
koefs = koefs.replace(' ',',')
while koefs.find(',,')!=-1:
    koefs = koefs.replace(',,',',')
koefs = koefs.split(',')
koefs = polyprep(koefs)
print(koefs)
koefs1=input('input coeffs2')
koefs1 = koefs1.replace(' ',',')
while koefs1.find(',,')!=-1:
    koefs1 = koefs1.replace(',,',',')
koefs1 = koefs1.split(',')
koefs1 = polyprep(koefs1)
print(koefs1)





#сумма многочленов
def polysum(koefs,koefs1):
    koefs2 = []
    if len(koefs)>len(koefs1):
        l=len(koefs)-len(koefs1)
        for i in range(l+1):
            koefs1.append(0)
    else:
        l = len(koefs1) - len(koefs)
        for i in range(l):
            koefs.append(0)
    for i in range(len(koefs)):
        a=int(koefs[i])
        b=int(koefs1[i])
        c=a+b
        koefs2.append(c)
    return koefs2
#конец функции суммы многочленофф


def polyprod(koefs,koefs1):
    c=[0]*(len(koefs)+len(koefs1)-1)
    for i in range(len(koefs)):
        for j in range(len(koefs1)):
            c[i+j]+=koefs[i]*koefs1[j]
    return c

def polysubstr(koefs,koefs1):
    koefs2 = []
    if len(koefs)>len(koefs1):
        l=len(koefs)-len(koefs1)
        for i in range(l+1):
            koefs1.append(0)
    else:
        l = len(koefs1) - len(koefs)
        for i in range(l):
            koefs.append(0)
    for i in range(len(koefs)):
        a=int(koefs[i])
        b=int(koefs1[i])
        c=a-b
        koefs2.append(c)
    return koefs2

def xx(a):
    b=[]
    for i in range(len(a)):
        b.append(str(a[i]))
        if i != 0:
            if i!=1:
                b.append('x')
                b.append('^')
                b.append(str(i))
            else:
                b.append('x')
        else:
            b.append('')
        if i+1<len(a) and int(a[i+1])>=0:
            b.append('+')
        else:
            b.append('')
    return ''.join(b)


print(xx(koefs))
print(xx(koefs1))
print(xx(polysum(koefs,koefs1)))
print(xx(polyprod(koefs,koefs1)))
print(xx(polysubstr(koefs,koefs1)))
#    koefs.append(int(input()))