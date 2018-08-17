def diamond(n):
    output = ''
    for i in range(0,n):
        if i<=n//2:
            output+=' '*(n//2-i)
            output+='*'*(2*i+1)
            output+='\n'
        else:
            output+=' '*(i-n//2)
            output+='*'*(2*(n-i)-1)
            output+='\n'
    return output


print(diamond(2))