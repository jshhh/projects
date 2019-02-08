n=int(input())
stakan1=input()
stakan1, ntemp = stakan1.split(' ')
stakan1 = int(stakan1)
stakan2 = 0
stakan3 = 0
b=0
c=0
e=0
while e<n-1:
    e += 1
    iphone = input()
    m,l = iphone.split(' ')
    iphone = int(m)
    if iphone>=stakan1:
        if(stakan2>0):
            stakan3 = stakan2
            nt2 = nt1
        stakan2 = stakan1
        nt1 = ntemp
        stakan1 = iphone
        ntemp = l
    elif iphone>=stakan2:
        if (stakan2 > 0):
            stakan3 = stakan2
            nt2 = nt1
        stakan2 = iphone
        nt1 = l
    elif iphone>=stakan3:
        stakan3 = iphone
        nt2 = l
print(stakan1, ntemp)
print(stakan2, nt1)
print(stakan3, nt2)