#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void pricti(int* a_p, int b){
	/* zvìtšit cislo a o cislo b */
	*a_p = *a_p + b;
}

int secti(int a, int b){
	/* seèti cislo a a cislo b */
	return a+b;
}

int secti_pole(int *pole){
	pole[0] += pole[1] + pole[2];
	return pole[0];
}

int main(int argc, char *argv[]) {	
	int cislo = 50;	
	int * adresa_integer = &cislo;
	int tri_cisla[3] = {10,20,30};
	
	char znak = 'P';
	char napis[] = {'A', 'h', 'o', 'j', '\0'}; // "Ahoj";
	
	printf("%s \n", napis);
	
	tri_cisla[1] = 200;
	printf("Druhe cislo v poli: %d \n", tri_cisla[1]);	
	printf("Druhe cislo v poli: %d \n", *(tri_cisla+1));
	
	printf("Prvni cislo v poli: %d \n", tri_cisla[0]);
	secti_pole(tri_cisla);
	printf("Prvni cislo v poli: %d \n", tri_cisla[0]);
	
	
	printf("Pointer: %p \n", adresa_integer);
	printf("Cislo: %10d pres pointer: %d \n", cislo, *adresa_integer);
	
	printf("Soucet: %d \n", secti(3,2));
		
	pricti(&cislo, 10); /* možnost 1 */ // cislo = secti(cislo, 10); /* možnost 2 */
	printf("Zvetsene: %d \n", cislo);
	
	
	system("pause");
	return 0;
}
