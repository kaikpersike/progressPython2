# maior elemento e index
a  = [int(s) for s in input().split()]
maior = a[0]
ind=0
for i in range(len(a)-1):
    if a[i+1] > maior:
        maior = a[i+1]
        ind = i+1
    
        
print(maior, ind)