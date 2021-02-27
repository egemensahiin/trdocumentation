// program 0'dan 100'e kadar olan sayıların toplamını hesaplıyor.
//
#include <stdio.h>

int main(){

	int sayac = 1;
	int toplam = 0;

	while(sayac <= 100){
		toplam += sayac;
		sayac++;
	}

	printf("1'den 100'e kadar olan sayiların toplami: %d\n", toplam);

	return 0;

}
