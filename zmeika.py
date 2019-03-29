from random import randint

a = [1]
maxlength = 40


def eat(aaa, b):
    if b>aaa[len(a)-1]:
        aaa.append(b)
        # print('yummy!!!')
    else:
        i = len(aaa)-1
        while i>=0 and b<aaa[i]:
            i-=1
        if i>=0:
            a.insert(i+1,b)
            # print('yummy!!!')
    if len(a)>maxlength:
        del a[0]


aa = []
for i in range(randint(1, 1000000)):
    food = randint(1, 200)
    aa.append( food)
    # eat(a, food)
    # print(food)


aa = sorted(aa)
print(aa[0:-4:])
if len(a)>maxlength:
    print('Obozhralas!')

