# troca de vizinho
a = [int(s) for s in input().split()]
lista=[]
for i in range(len(a)-1):
    if i%2==0:
        lista.append(str(a[i+1]))
        lista.append(str(a[i]))

if len(a)%2!=0 and len(a)>1:
    lista.append(str(a[-1]))
    print(' '.join(lista))
if len(a)%2==0:
    print(' '.join(lista))
if len(a) == 1:
    print(a[0])