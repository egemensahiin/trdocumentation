// verilen iki sayinin obebini bulur (bulabilirse tabii)

#include <stdio.h>

int main(){

	int kalan = -1;
	int buyuk, kucuk, yedek;

	printf("OBEB'lerini hesaplamak üzere iki adet sayi giriniz:");
	scanf("%d%d", &buyuk, &kucuk);
	printf("---------------------\n");

	if (kucuk > buyuk){
		yedek = kucuk;
		kucuk = buyuk;
		buyuk = yedek;
	}

	while (kalan != 0){
		kalan = buyuk % kucuk;
		buyuk = kucuk;
		if (kalan != 0)
			kucuk = kalan;
	}

	printf("Verilen iki sayinin OBEB'i: %d\n", kucuk);

}
