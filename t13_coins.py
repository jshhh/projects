change=int(input('сдача:'))
k=int(input('количество номиналов:'))
nom=[]
for i in range(k):
    nom.append(int(input()))
ch=change
nom = sorted(nom)
print(nom)
amount=0
while ch!=0:
    if ch//nom[len(nom)-1]!=0:
        amount+=ch//nom[len(nom)-1]





