def mcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

resultado = mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es {resultado}")