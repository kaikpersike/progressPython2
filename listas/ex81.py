# Boliche
n, k = [int(s) for s in input().split()]
pin = ["I"]*n
#print(pin)
for i in range(k):
    a, b = input().split()
    a = int(a)
    b = int(b)
    for j in range(a-1, b):
        #print(j)
        pin[j]="."
print(''.join(pin))
# for i in range(k):
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
