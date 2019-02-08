s=['mama','mila','ramu']
t=''
i=0
for i in range(len(s)):
        t+=s[i]
        if i!=len(s)-1:
            t+=' '
print(t)