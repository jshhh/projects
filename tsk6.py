from random import randint

#config
mode = 'AUT'

def digitInput(prompt='',bounds=(0,100)):
    if mode=='AUTO':
        out = randint(bounds[0],bounds[1])
    else:
        out = int(input(prompt))
    print('INPUT',out)
    return out


total_amount=digitInput()
first_number=digitInput()
amount_of_doubles=0
d=0

def amount_of_digits(number):
    n = 0
    while number > 0:
        n += 1
        number = number // 10
    return n

n = amount_of_digits(first_number)

for i in range(total_amount-1):
    current_number=digitInput(bounds=(0,100000))
    d = amount_of_digits(current_number)
    if d>n:
        n = d
        amount_of_doubles = 0
    if d==n:
        amount_of_doubles += 1


print(n, amount_of_doubles)