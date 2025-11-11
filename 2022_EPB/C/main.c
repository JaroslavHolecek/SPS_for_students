#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

/* pøedávání argumentù hodnotou */
int secti(int a, int b){
	return a+b;
}

/* pøedávání argumentù odkazem */
void pricti(int * a_p, int b){
	*a_p = *a_p + b;
}

int soucet_pole(int *pole){
	pole[0] += pole[1];
	pole[0] += pole[2];	
	return pole[0];
}

int main(int argc, char *argv[]) {
	int cislo = 50;
	int *ukazatel = &cislo;
	int tri_cisla[3] = {10,20,30};
	
	char pismeno = 'A';
	/*string*/ char text[] = {'A', 'h', 'o', 'j', '\0'};
	char text2[] = "Ahoj";
	text2[4] = 'A'; /* prepsani nuloveho/koncoveho znaku -> nyni jiz printf nepozna, kde text2 konci */
	
	printf("%s\n%s\n", text, text2);
	
	printf("Prvni cislo pole: %d \n", tri_cisla[0]);
	int vysledek = soucet_pole(tri_cisla);
	printf("Vysledek: %d \n", vysledek);
	printf("Prvni cislo pole: %d \n", tri_cisla[0]);
	
	printf("Cislo: %10d, pres pointer: %d \n", cislo, *ukazatel);
	printf("Pointer: %p \n", ukazatel);
	
	vysledek = secti(cislo, 5);
	printf("Vysledek scitani: %d \n", vysledek);
	cislo = secti(cislo, 5); /* zmìna hodnoty -> kopirovani sem a tam */
	printf("Cislo: %d \n", cislo);
	pricti(&cislo, 20);	/* zmìna hodnoty -> bez kopirovani sem a tam */
	printf("Cislo: %d \n", cislo);
	
	
	system("pause"); /* Pro ponechani otevrene konzole po skonceni programu */
	return 0;
	
}


