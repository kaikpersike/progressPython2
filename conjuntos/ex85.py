b = set()
for i in [int(s) for s in input().split()]:
    if i in b:
        print("YES")
    else:
        print("NO")
        b.add(i)