// klavyeden negatif bir sayi girilene kadar verilen sayilardan en buyuk ve
// en kucugunu yazan program

#include <stdio.h>

int main(){

	long sayi, max, min;

	printf("Bir sayi girin (sonlandirmak icin negatif): ");
	scanf("%ld", &sayi);

	while(sayi > 0){ // do-while kullanmak istesek de do-while'da komutlar çalıştıktan
		// sonra kontrol yapıldığı için verilen negatif sayı her zaman en küçük olur.

		if(sayi > max)
			max = sayi;
		if(sayi < min)
			min = sayi;

		printf("Bir sayi girin (sonlandirmak icin negatif): ");
		scanf("%ld", &sayi);

	}

	printf("--------------------\n");
	printf("Girilen sayilarin en buyugu: %ld\n", max);
	printf("Girilen sayilarin en kucugu: %ld\n", min);

}
