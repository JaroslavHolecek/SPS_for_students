#include <windows.h>
#include <iostream>

typedef int (*AddFunc)(int, int);

int main() {
    HINSTANCE hDll = LoadLibraryA("mymath.dll");
    if (!hDll) {
        std::cerr << "Chyba při načítání DLL" << std::endl;
        return 1;
    }

    AddFunc add = (AddFunc)GetProcAddress(hDll, "add");
    if (!add) {
        std::cerr << "Funkce add nenalezena" << std::endl;
        FreeLibrary(hDll);
        return 1;
    }

    int result = add(5, 7);
    std::cout << "5 + 7 = " << result << std::endl;
    scanf("%d");

    FreeLibrary(hDll);
    return 0;
}

/* g++ -o main.exe main.cpp */
