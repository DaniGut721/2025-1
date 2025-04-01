def g(x, y):
    """Función ejemplo: división de x entre y multiplicada por suma"""
    return (x + y) * (x / y)

def main():
    print("Calculadora de función g(x, y) - Valores distintos de cero")
    
    while True:
        try:
            x = float(input("\nIngrese el valor de x (distinto de 0): "))
            if x == 0:
                print("Error: x no puede ser cero")
                continue
                
            y = float(input("Ingrese el valor de y (distinto de 0): "))
            if y == 0:
                print("Error: y no puede ser cero")
                continue
                
            resultado = g(x, y)
            print(f"\nResultado de g({x}, {y}) = {resultado:.2f}")
            
        except ValueError:
            print("Error: Debe ingresar valores numéricos")
        except ZeroDivisionError:
            print("Error: La operación genera una división por cero")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
        
        continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if continuar != 's':
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()