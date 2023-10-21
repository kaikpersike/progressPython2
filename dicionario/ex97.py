dic = dict()
for i in range(int(input())):
    ingles, latim= input().split(' - ')
    latim_ingles = latim.split(', ')

    for i in latim_ingles:
        if i in dic:
            dic[i] = dic[i]+", "+ingles
        else:
            dic[i] = ingles
print(len(dic))
for k, v in sorted(dic.items()):
    print(k, "-", v)