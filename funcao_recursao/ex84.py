#1º letra miuscula
def capitalize():
    a = [str(s) for s in input().split()]
    for i in range(len(a)):
        a[i] = a[i].capitalize()
    print(' '.join(a))

capitalize()