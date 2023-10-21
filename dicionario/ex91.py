dados = dict()
for i in range(int(input())):
    a,b = input().split()
    dados[a] = b
    
c = input()
for k, v in dados.items():
    if v == c:
        print(k)
    elif k == c:
        print(v)