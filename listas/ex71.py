# mais alto que anterior
a = [int(s) for s in input().split()]
lista=[]
for i in range(len(a)-1):
    if a[i]< a[i+1]:
        print(a[i+1], end=" ")