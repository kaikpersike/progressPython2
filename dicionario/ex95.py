dic = dict()
for i in range(int(input())):
    pais = input().split()
    dic[pais[0]] = pais[1:]

for i in range(int(input())):
    cidade = input()
    for k, v in dic.items():
        if cidade in v:
            print(k)
        