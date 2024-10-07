'''
deret fibonacci = 0 1 1 2 3 5 8 13 21 34 .....

f(1) = 0
f(2) = 1
f(3) = f(2) + f(1)
f(n) = f(n-1) + f(n-2)

'''

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,11):
    print(fibonacci(i), end=" ")

    