# define function to get a fibonacci series
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    

# get input for fibonacci function
fibonacci(int(input("Enter a number to get fibonacci series: ")))