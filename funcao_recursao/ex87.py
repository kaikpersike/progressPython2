#Fibonacci

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
print(fib(int(input())))

# 0 1 1 2 3 5 8- quero isso
#   1 2 3 4 5 6