# intersection
a = set(input().split())
b = set(input().split())
teste = list(a&b)
teste.reverse()
print(teste)

print((list((set(input().split()) & set(input().split())))).sort())