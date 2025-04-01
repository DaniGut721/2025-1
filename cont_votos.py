import os
try:
    from msvcrt import getch
except ImportError:
    # Para sistemas que no sean Windows
    import sys, tty, termios
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

cont1 = cont2 = cont3 = cont4 = cont5 = 0.0
suma = 0.0

while True:
    print("lista1, lista2, lista3, lista4, lista5")
    voto = input("\nIngrese su voto: ")
    try:
        voto = int(voto)
    except ValueError:
        voto = 6  # Tratar como voto inválido

    if voto <= 4:
        if voto <= 2:
            if voto == 2:
                cont2 += 1
            else:
                cont1 += 1
        else:
            if voto == 4:
                cont4 += 1
            else:
                cont3 += 1
    else:
        cont5 += 1

    print("\nDesea salir? (S/N)")
    rpt = getch().decode().upper() if isinstance(getch(), bytes) else getch().upper()
    if rpt == 'S':
        break
    os.system('cls' if os.name == 'nt' else 'clear')

suma = cont1 + cont2 + cont3 + cont4 + cont5
print("\nResultados al 100%:")
print(f"lista1 = {(cont1 * 100.0 / suma):.2f}%")
print(f"lista2 = {(cont2 * 100.0 / suma):.2f}%")
print(f"lista3 = {(cont3 * 100.0 / suma):.2f}%")
print(f"lista4 = {(cont4 * 100.0 / suma):.2f}%")
print(f"lista5 = {(cont5 * 100.0 / suma):.2f}%")

# Esperar tecla para salir
getch()