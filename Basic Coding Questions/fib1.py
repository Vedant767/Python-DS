def fib(num):
    sum = 1
    for i in range(1,num + 1):
        sum = sum * i
    
    return sum


print(fib(5))