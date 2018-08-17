# -*- coding: utf-8 -*-
words=[]
amounts=[]
try:
    with open("t1.txt") as f:
        for line in f:
            for word in line.split():
                if word in words:
                    pos = words.index(word)
                    amounts[pos]+=1
                else:
                    words.append(word)
                    amounts.append(1)

    print(words)
    print(amounts)

except FileNotFoundError:
    print('file not found')

