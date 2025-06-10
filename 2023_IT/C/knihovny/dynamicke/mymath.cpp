// mymath.cpp
#include <windows.h>

extern "C" __declspec(dllexport) int add(int a, int b) {
    return a * b;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    return TRUE;
}

/* kompilace dymanické knihovny na windows */
/* g++ -shared -o mymath.dll mymath.cpp  */