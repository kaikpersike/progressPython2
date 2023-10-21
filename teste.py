res = [''.join(input().split()), ".txt"]
res=''.join(res) 

valores_celulares = [850, 2230, 1500, 3500, 5000]
with open(res, 'w') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor)+'\n')

# valores_celulares = [850, 2230, 1500, 3500, 5000]
# with open('res', 'r') as arquivo:
#     for valor in arquivo:
#         print(valor)