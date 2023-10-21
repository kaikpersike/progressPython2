# Queen to queen
teste = 0
lista_a = []
lista_b = []
for i in range(8):
    a, b = [int(s) for s in input().split()]
    lista_a.append(a)
    lista_b.append(b)

for i in range(8):
    for j in range(i+1,8):
        if lista_a[i] == lista_a[j] or lista_b[i] == lista_b[j] or abs(lista_a[i]-lista_a[j]) == abs(lista_b[i]-lista_b[j]):
            teste=1
if teste == 1:
    print("YES")
else:
    print("NO")
