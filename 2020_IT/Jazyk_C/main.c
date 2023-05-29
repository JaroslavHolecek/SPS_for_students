#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */


#define E 2.71828
#define SOUCET_TRI(x,y,z) x+y+z

int main(int argc, char *argv[]) {
	
	printf("E je (na 5 des. mist): %f\n ", E);
	
	printf("Soucet je: %d\n", SOUCET_TRI(5, 6, 7)); 
	printf("Soucet je: %f\n", SOUCET_TRI(5.1, 6.2, 7.3)); 
	
	printf("Ahoj"); 	
	printf("Studenti");
	
	int cele_cislo = 5;
	int druhe;
	druhe = 10;
	
	char znak = "A";
	float desetinne = 2.71;

	
	if (cele_cislo == 5)
	{
		printf("Je rovno peti"); 
	}else
	{
		printf("Není rovno peti");
	}
	int cele_cislo_while = 5;
	while (cele_cislo_while > 0)
	{
		printf("%d", cele_cislo_while);
		cele_cislo_while--;
	}
	
	printf("Staticke pole:\n");
	int pole_ctyr[4];
	int pocitadlo;	
	for(pocitadlo = 0; pocitadlo < 4; pocitadlo++ )
	{
		printf("%d  ", pole_ctyr[pocitadlo] );	
	}
	
	char retezec[] = "Ahoj";
		
	
	return 0;	
}
