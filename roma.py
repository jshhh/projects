def decoder(n):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    a = 0
    if len(n)==1:
        a=d[n]
    else:

        for i in range(0, len(n) - 1):
            if d[n[i]] >= d[n[i + 1]]:
                a += d[n[i]]
            elif d[n[i]] < d[n[i + 1]]:
                a -= d[n[i]]
    a += d[n[len(n)-1]]
    return a


print(decoder('LXXXIV'))