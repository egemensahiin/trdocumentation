// iki basamakli en buyuk ikiz asal sayi ciftini bulan program
// aslinda bu program en iyi bir asalMi fonksiyonu ile yapılır da
// simdinin konusu degil.

#include <stdio.h>

int main(){

	int i, j;
	int test1 = 1, test2 = 1;

	printf("Aradiginiz sayilar: ");

	for(i = 99; i >= 12; i--){
		for(j = i - 1; j > 1 && test1 == 1; j--){ // i'nin asalliginin kontrolu
			if(i % j == 0)
				test1 = 0;
		}
		for(j = i - 3; j > 1 && test2 == 1; j--){ // i - 2'nin asalliginin kontrolu
			if((i - 2) % j == 0)
				test2 = 0;
		}
		if(test1 == 1 && test2 == 1){ // Eger herhangi bir cifte denk gelirse bunlari yaz ve
			printf("%d ve %d", i, i - 2); // donguyu sonlandir ki bosa calismasin.
			break;
		}
		test1 = 1; // Eger biri asal digeri degilse yani if kosulu, break komutuna kadar
		test2 = 1; // gelemediyse test degerlerini default degerlere ata.
	}

	return 0;

}
