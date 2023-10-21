# poliglota

n1 = int(input()) #nº de estudantes
universo = set()
comparacao = set()
interseccao = set()
for i in range(n1):
    n2 = int(input()) #nº de linguas / estudantes
    for j in range(n2):
        linguas = input() #linguas faladas
        comparacao.add(linguas) # add linguas para comparacao de interseccao
        universo.add(linguas) # add linguas total faladas
    interseccao= comparacao&universo # assumindo valor para interseccao
    comparacao = set() # resetando valor de comparacao para receber novos valores
lista = list(interseccao)
lista.sort()
lista2 = list(universo)
lista2.sort()
print(len(lista))
for i in lista:
    print(i)
print(len(lista2))
for i in lista2:
    print(i)

