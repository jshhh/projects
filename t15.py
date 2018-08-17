x=int(input())
y=int(input())
z=int(input())
a=0
uslovie = False
if x!=y:
    if y!=z:
        if x!=z:
            if (x+y+z)/2>1:
                if x<z:
                    uslovie = True
                    x=(y+z)/2
                else:
                    uslovie = True
                    z=(x+y)/2
if not uslovie:
    if x>y:
        if x>z:
            a=x
        else:
            a=z
    else:
        if y>z:
            a=y
        else:
            a=z
    if x<y:
        if x<z:
            x=a
        else:
            z=a
    else:
        if y<z:
            y=a
        else:
            z=a
print(x)
print(y)
print(z)