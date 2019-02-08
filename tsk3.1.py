amount=int(input('vviditi kolidstvo disel'))
currentmin1=int(input())
currentmin2=int(input())
for i in range(0,amount-2):
    b=int(input())
    if currentmin1>b:
        if currentmin2<b:
            currentmin2=b
    else:
        currentmin1 = b
print(currentmin1,currentmin2)
