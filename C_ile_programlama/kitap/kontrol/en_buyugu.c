// verilen 3 sasayi2idan en busayi2ugunu sayi2asayi3ar.
//
#include <stdio.h>

int main(){

	float sayi1, sayi2, sayi3;
	float enBuyuk;
	
	printf("3 adet sayi giriniz: ");
	scanf("%f%f%f", &sayi1, &sayi2, &sayi3);

	enBuyuk = sayi1;

	if(sayi2 > enBuyuk)
		enBuyuk = sayi2;
	if(sayi3 > enBuyuk)
		enBuyuk = sayi3;

	printf("Verilen uc sayidan en buyugu %.2f\n", enBuyuk);

}
