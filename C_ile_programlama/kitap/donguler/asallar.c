// 1 ile x arasindaki asal sayilari bulur.
//
#include <stdio.h>

int main(){

	int bitis, asal = 1;
	int i, j;

	printf("Bitis noktasi giriniz: ");
	scanf("%d", &bitis);
	printf("---------------------------\n");
	printf("1 ile %d arasindaki asal sayilar: ", bitis);

	for(i = 1; i <= bitis; i++){
		if(i == 1){ // i = 1 oldugunda hicbi sey yapmadan basa dön. bu sayi olarak 1 girilmesi
			continue; // ihtimali icin iyi yoksa gereksiz, dongu 2den de baslatilabilirdi.
		}
		for(j = i - 1; j > 1 && asal == 1; j--){ // 18-20. satirlar, i'nin asalliginin kontrolu
			if(i % j == 0)
				asal = 0;
		}
		if(asal) // eger i asal ise i'yi yazdir.
			printf("%d, ", i);
		asal = 1; // i'nin durumunu kontrol ettikten sonra yeni döngü degiskeninde testi defaulta al
	}
	return 0;
}
