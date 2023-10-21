nomes = dict()

for i in range(int(input())):
    a, b = input().split()
    b = int(b)
    if a not in nomes:

        nomes[a] = b
    else:
        nomes[a]+=b
for candidato, votos in sorted(nomes.items()):
    print(candidato, votos)