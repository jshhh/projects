import random


def multiple(var1, var2, var5, n):
    if n % 10 == 1:
        return var1
    if n % 10 in [2, 3, 4]:
        return var2
    if n % 10 in [5, 6, 7, 8, 9, 0]:
        return var5


def palochka(n):
    if n % 4 == 1:
        z = random.randint(1, 3)
    else:
        z = (n % 4 + 4 - 1) % 4
    return z


n = random.randint(15, 170)
while n > 0:
    n -= palochka(n)
    if n <= 0:
        print('вы победили')
        exit(0)
    print("осталось ", n, " ", multiple("палочка", "палочки", "палочек", n), ". ваш ход:")
    n -= int(input())

print('вы проиграли')
