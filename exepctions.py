a=[1,2,3]

try:

    raise IndexError
    x = 4 / 0

    for i in range(10):
        print(a[i])


except IndexError:
    print('Все ок, мы ее поймали')
except ZeroDivisionError:
    print('Операция не определена')
print('прога идет дальше')

