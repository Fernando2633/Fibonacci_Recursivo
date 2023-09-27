def fibonacci_recursive(Num):
    if Num <= 0:
        return []
    elif Num == 1:
        return [1]
    elif Num == 2:
        return [1, 1]
    else:
        fibo = fibonacci_recursive(Num - 1)
        next = fibo[-2] + fibo[-1]
        fibo.append(next)
        return fibo

n = input("Ingresa un número de la sucesión de Fibonacci: ")
n = int(n)
result = fibonacci_recursive(n)
print(result)
