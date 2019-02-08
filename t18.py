a1=0
a2=0
a2=0;
s1=''
s2=''
s3=''
for i in range(1,n):
    read(a,s);
    if a>a1:
        if s=s1:
            a1=a
            s1=s
        elif s=s2:
            a2=a1;
            s2=s1;
            a1=a;
            s1=s
    else:
        a3=a2;
        a2=a1;
        s3=s2;

s2=s1
a1=a
s1=s
 else if a>a2 then begin

if s=s2 then begin s2:=s; a2:=a; end

else if (s<>s1) then begin

a3:=a2;

s3:=s2;

a2:=a;

s2:=s;

end;

else if a>a3:
    if (s<>s1) and (s<>s2):
        a3=a
        s3=s
print('1 место.',s1,' (',a1,')');
print('2 место.',s2,' (',a2,')');
print('3 место.',s3,' (',a3,')');
