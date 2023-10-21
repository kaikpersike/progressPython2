palavras = dict()
for i in range(int(input())):
    a = input().split()
    for j in a:

        if j not in palavras:
            palavras[j] = 1
        else:
            palavras[j] +=1
# print(palavras.values())
maior = 0
x = dict()
for k, v in sorted(palavras.items()):
    if v> maior:
        maior = v
        x=k
print(x)
    
"""
1
apple orange banana banana orange

= banana
"""
"""
3
q w e r t y u i o p
a s d f g h j k l
z x c v b n m

= a
"""