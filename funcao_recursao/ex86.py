#reversao
def valor():
    a=int(input())
    if a ==0:
        print(a)
    else:
        valor()
        print(a)
valor()
