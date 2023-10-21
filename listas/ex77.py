# change min to max
a = [int(s) for s in input().split()]
maior = a[0]
menor = a[0]
ind = 0
ind2 = 0
for i in range(len(a)):
    if maior<a[i]:
        maior=a[i]
        ind=i
    if menor>a[i]:
        menor = a[i]
        ind2 = i

a[ind] = menor
a[ind2] = maior
print(a)