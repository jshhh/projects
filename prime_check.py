import math

num = 2 ** 31-3
c = 0
for i in range(2, int(math.sqrt(num) + 1)):
    if num % i == 0:
        c += 1
        print(i)
if c == 0:
    print('простое')
else:
    print('составное')
print(num,c)
