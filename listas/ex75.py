# nº distinto
a = [int(s)for s in input().split()]
cont=0
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        cont+=1
print(cont+1)