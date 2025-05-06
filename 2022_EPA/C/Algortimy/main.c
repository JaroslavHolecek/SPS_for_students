#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int max(int* arr, int delka){
	int max_hodnota = arr[0];
	int i;
	for (i = 1; i<delka; i++){
		if(arr[i]>max_hodnota){
			max_hodnota = arr[i];
		}
	}
	return max_hodnota;
}


int main(int argc, char *argv[]) {
	
	printf("nejvìtší prvek v poli je: %d",max({1,657,657,8756,8856,-564}, 6));
	
	
	
	return 0;
	
	
}
