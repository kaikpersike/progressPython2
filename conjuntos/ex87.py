# a = {"She", "sells", "sea", "shells", "on", "the", "sea", "shore;"}
# b = {"The", "shells", "that", "she", "sells", "are", "sea", "shells", "I'm sure."}
# c = {"So", "if", "she", "sells", "sea", "shells", "on", "the", "sea", "shore,"}
# d = {"I'm", "sure", "that", "the", "shells", "are", "sea", "shore", "shells."}
# e = a|b
# print(len(e))
# f = c|d
# print(len(f))
# g = e|f
# print(len(g)) # mostra os elementos distindos

n = int(input())
b = set()
for i in range(n):
    a = set(str(s) for s in input().split())
    for j in a:
        b.add(j)
print(len(b))