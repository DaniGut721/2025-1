#include <iostream>
#include <cctype>
#include <limits>

using namespace std;

int main()
{
    int voto;
    float cont1 = 0, cont2 = 0, cont3 = 0, cont4 = 0, cont5 = 0, suma;
    char rpt;

    do {
        cout << "lista1, lista2, lista3, lista4, lista5" << endl;
        cout << "\nIngrese su voto: ";
        cin >> voto;

        // Limpiar el buffer de entrada
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        if(voto <= 4)
        {
            if(voto <= 2)
            {
                if(voto == 2) cont2 = cont2 + 1;
                else cont1 = cont1 + 1;
            }
            else 
            {
                if(voto == 4) cont4 = cont4 + 1;
                else cont3 = cont3 + 1;
            }
        }
        else 
        {
            cont5 = cont5 + 1;
        }

        cout << "\nDesea salir? (S/N): ";
        cin >> rpt;
        rpt = toupper(rpt);

        // Limpiar pantalla (alternativa multiplataforma)
        #ifdef _WIN32
            system("cls");
        #else
            system("clear");
        #endif

    } while(rpt != 'S');

    suma = cont1 + cont2 + cont3 + cont4 + cont5;
    cout << "\nResultados al 100%: " << endl;
    cout << "lista1 = " << cont1 * 100.0/suma << "%" << endl;
    cout << "lista2 = " << cont2 * 100.0/suma << "%" << endl;
    cout << "lista3 = " << cont3 * 100.0/suma << "%" << endl;
    cout << "lista4 = " << cont4 * 100.0/suma << "%" << endl;
    cout << "lista5 = " << cont5 * 100.0/suma << "%" << endl;

    cout << "\nPresione Enter para salir...";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cin.get();

    return 0;
}