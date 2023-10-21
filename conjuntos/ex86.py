n, m = [int(s) for s in input().split()]
alice = set()
bob = set()
for i in range(n):
    x = int(input())
    alice.add(x)
for i in range(m):
    y = int(input())
    bob.add(y)

lista_ab = list(alice&bob) #interseccao
lista_ab.sort()
print(len(lista_ab))
for i in lista_ab:
    print(i)

lista_a = list(alice-(alice&bob)) #incluido no a, mas nao na intersec
lista_a.sort()
print(len(lista_a))
for i in lista_a:
    print(i)

lista_b = list(bob-(alice&bob))
lista_b.sort()
print(len(lista_b))
for i in lista_b:
    print(i)

