def procesar_numero(numero):
    # Convertir a cadena y eliminar signos y puntos
    str_num = str(numero).replace('-', '').replace('.', '')
    digitos = [int(c) for c in str_num if c.isdigit()]
    
    if not digitos:
        return None, None  # Caso de entrada inválida
    
    return min(digitos), max(digitos)

def main():
    print("Calculadora de cifras mínima y máxima")
    
    while True:
        entrada = input("\nIngrese un número (entero o decimal): ").strip()
        
        try:
            # Convertir a float o int según corresponda
            num = float(entrada)
            if num.is_integer():
                num = int(num)
        except ValueError:
            print("Error: Debe ingresar un número válido")
            continue
            
        min_dig, max_dig = procesar_numero(num)
        
        if min_dig is None:
            print("El número no contiene dígitos válidos")
        else:
            print(f"\nPara el número {num}:")
            print(f"Cifra más pequeña: {min_dig}")
            print(f"Cifra más grande: {max_dig}")
        
        continuar = input("\n¿Desea ingresar otro número? (s/n): ").lower()
        if continuar != 's':
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()