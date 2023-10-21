#Expoente
def base(a):
    def expo(n):
        if n ==0:
            return 1
        else:
            return a * expo(n-1)
    print(expo(float(input())))
base(float(input())) 
