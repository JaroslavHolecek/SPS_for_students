#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	printf("nejmensi cislo je: %d", MinZeTri(2, 5, 17));
	return 0;
}
int minpole(int * p, int delka) {
	int nej = p[0];
    int i; 
	for (i = 1; i < delka; i += 1){
		p[i];
		if (p[i] < nej){
			nej = p[i];
	
		}
	}
	return nej;	
}



int MinZeTri(int x, int y, int z) {
	if (x < y){		  
        if (x < z){
            return x;
		}
        else{
        	return z;
		}            
	}
    else{
        if (y < z){
            return y;
        }
        else{
            return z;
		} 
    }
}



