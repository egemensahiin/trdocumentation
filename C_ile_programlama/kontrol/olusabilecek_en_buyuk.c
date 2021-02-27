// verilen 3 basamaklı bir tam sayıdan oluşturulabilecek en büyük 3 basamaklı tamsayiyi verir.
//
#include <stdio.h>

int main(){

	int girdi, cikti;
	int bas1, bas2, bas3;
	int yedek;

	printf("3 basamakli bir sayi giriniz: ");
	scanf("%d", &girdi);

	printf("--------------------------\n");

	bas1 = girdi % 10;
	bas2 = ((girdi %100) - bas1) / 10;
	bas3 = (girdi - (girdi % 100)) / 100;

	if(bas1 < bas2){
		yedek = bas1;
		bas1 = bas2;
		bas2 = yedek;
	}
	if(bas2 < bas3){
		yedek = bas2;
		bas2 = bas3;
		bas3 = yedek;
	}
	if(bas1 < bas2){
		yedek = bas1;
		bas1 = bas2;
		bas2 = yedek;
	}
	printf("Oluşabilecek en büyük sayi: %d\n", (bas1 * 100) + (bas2 * 10) + bas3);
	printf("Oluşabilecek en küçük sayi: %d\n", (bas3 * 100) + (bas2 * 10) + bas1);

	return 0;

}
