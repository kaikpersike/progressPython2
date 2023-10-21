# dic = input()
test=dict()
# print(dic[dic.find(" ")+1:]) valor
# print(dic[:dic.find(" ")]) chave
for i in range(int(input())):
    dic = input()
    test[dic[:dic.find(" ")]] = dic[dic.find(" ")+1:]
    print(test)
for i in range(int(input())):
    perm, valor = input().split()
    if perm == "read":
        perm = "R"
    elif perm == "write":
        perm = "W"
    else:
        perm = "X"
    
    if perm in test[valor]:
        print("OK")
    else:
        print("Access denied")

