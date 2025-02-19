def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

n = int(input("Introduce un numero para calcular su factorial: "))
resultado = factorial(n)
print(f"El factorial de {n} es {resultado}")        