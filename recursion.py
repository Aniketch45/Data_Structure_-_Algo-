#factorial
def facto(n):
    if n==1:
        return 1
    else:
        return n * facto(n-1)
    
num = facto(5)
print(num)

#fibonacci number

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
num = fib(7)
print(num)