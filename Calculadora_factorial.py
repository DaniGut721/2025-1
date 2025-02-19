print("Bienvenido a la calculadora de factoriales")
n = int(input("por favor ingresa un numero"))
if n < 0:
    print("el factorial del numero", n, "es: 0")
else:
    factorial = 1
    for i in range(1, n + 1, 1):
        factorial = factorial*i
print("el factorial del numero", n, "es: ", factorial)            