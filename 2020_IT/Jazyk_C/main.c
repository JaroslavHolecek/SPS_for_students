#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */


#define E 2.71828
#define SOUCET_TRI(x,y,z) x+y+z

void hodnotou(int x, int y)
{
	x = x+y;
	printf("x: %d \n", x);
}

void odkazem(int *x, int *y)
{
	*x = *x+*y;
	printf("x: %p \n", x);
	printf("*x: %d \n", *x);
}

int main(int argc, char *argv[]) {
	
	int rohliky = 10;
	int *rohliky_p = &rohliky;
	
	printf("rohliky: %d \n", rohliky);
	printf("rohliky_p: %p \n", rohliky_p);
	printf("*rohliky_p: %d \n", *rohliky_p);
	
	int A[5] = {10, 8, 6, 4, 2};
	printf("A: %p \n", A);
	printf("*A: %d \n", *A);
	
	printf("A[2]: %d \n", A[2]);
	printf("*(A+2): %d \n", *(A+2));
	printf("*A+2: %d \n", *A+2);
	
	int a = 3, b = 5;
	
	printf("Pred hodnotou a: %d b: %d \n", a, b);
	hodnotou(a,b);
	printf("Po hodnotou a: %d b: %d \n", a, b);
	
	printf("Pred odkazem a: %d b: %d \n", a, b);
	odkazem(&a,&b);
	printf("Po odkazem a: %d b: %d \n", a, b);
	
	
	/*
	
	
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
		
	*/
	return 0;	
}
