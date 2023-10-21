ordem = dict()

for i in range(int(input())):
  for palavra in input().split():
    if palavra in ordem:
        ordem[palavra]-=1
    else:
        ordem[palavra] =-1

# freqs = [(-valor, chave) for (chave, valor) in ordem.items()]
# freqs.sort()

# for v, k in freqs:
#      print(k)
lista=[]
for k,v in ordem.items():
   lista.append((v,k))

for i in sorted(lista):
   print(i[1])