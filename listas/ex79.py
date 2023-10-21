# lista com unico elemento
a = [int(s) for s in input().split()]
rep = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i != j:
            rep = a[j]
    if a[i] != rep:
        print(a[i], end=" ")

