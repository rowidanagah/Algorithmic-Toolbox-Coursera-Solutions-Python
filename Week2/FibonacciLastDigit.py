# Uses python3
def FibonacciLastDigit(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a
num = int(input())
print(FibonacciLastDigit(num))
