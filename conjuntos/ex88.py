n = int(input())

final = set(range(1, n+1))


nset = input()
while(nset != "HELP"):
    conj = set([int(v) for v in nset.split()])
    tipo = input()
    if tipo == "YES":
        final = final&conj
    else:
        final = final-conj
    nset = input()

saida = list(final)
saida.sort()

saida = map(str, saida)

print(" ".join(saida))