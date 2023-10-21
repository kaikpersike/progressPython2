palavras = input().split()
dic = {}
for palavra in palavras:
    print(dic.get(palavra, 0))
    dic[palavra] = dic.get(palavra, 0)+1
