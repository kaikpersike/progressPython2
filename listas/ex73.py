# maior que ambos os vizinhos
a = [int(s) for s in input().split()]
cont=0
for i in range(len(a)-2):
    if a[i+1] > a[i] and a[i+1] > a[i+2]:
        cont+=1
print(cont)