# Fibonacci module

def _welcome(message): # just a welcome message but not import with *
    print(message)

def get_fibo(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def print_fibo(n): # print all fibonacci series up to n
    fibo_series = get_fibo(n)
    for fibo in fibo_series:
        print(fibo, end=' ')
    print()
