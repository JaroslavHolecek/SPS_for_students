#include <iostream>

int hlavni()
{
    std::cout << "Hello World" << std::endl;
    scanf("%d");

    return 0;
}

/* nazev_kompilatoru nazev_souboru_se_zdrojovym_kodem -o nazev_vystupniho_souboru/spustitelneho_programu */
/* g++ helloworld.cpp -o mujprogram.exe */

/* -c spusti pouze část kompilace, nevytvoří .exe soubor, poté můžu z připraveného .o souboru vytvořit .exe  */
/* g++ -c helloworld.cpp -o helloworld.o   */
/* g++ helloworld.o -o mujprogram2.exe   */