expression = input('input expression: ')
digits = list(range(10))

a=[]
b=[]

buf=0
for i in range(len(expression)):
    l=expression[i]
    try:
        buf=buf*10+int(l)
    except ValueError:
        a.append(buf)
        a.append(l)
        buf=0
if buf>0:
    a.append(buf)
for i in range(len(a)):
    if a[i]!='-' and a[i]!='+' and a[i]!='*' and a[i]!='/' :
        b.append(a[i])
for j in range(len(a)):
    if a[j] == '-' or a[j] == '+' or a[j] == '*' or a[j] == '/':
        b.append(a[j])


print(a)
print(b)