#include <stdio.h>
#include <time.h>
#include <stdlib.h>


void renkMesajiYaz(int a);

int main(){
	srand(time(NULL));
	renkMesajiYaz(2);
	renkMesajiYaz(1);
	renkMesajiYaz(5);
	return 0;
}

void renkMesajiYaz(int a){
	int rastgeleRenk;
	do{
		rastgeleRenk = rand() % 9;
	}while (rastgeleRenk == a);
	printf("Hic begenmedim!\n");
	switch(rastgeleRenk){
		case 0:
			printf("Siyah ");
			break;
		case 1:
			printf("Kahverengi ");
			break;
		case 2:
			printf("Kirmizi ");
			break;
		case 3:
			printf("Turuncu ");
			break;
		case 4:
			printf("Sari ");
			break;
		case 5:
			printf("Yesil ");
			break;
		case 6:
			printf("Mavi ");
			break;
		case 7:
			printf("Mor ");
			break;
		case 8:
			printf("Gri ");
			break;
		case 9:
			printf("Beyaz ");
			break;
	}
	printf("renge boyayin.\n");
}
