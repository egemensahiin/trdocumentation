// standart fonksiyonların denenmesi:

#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>

int main(){

	int i;

	/* Math kutuphanesindeki fonksiyonlar */
	printf("%.2lf\n", sqrt(25.0));
	printf("%.2lf\n", exp(1.0));
	printf("%.2lf\n", log(2.718282));
	printf("%.2lf\n", log10(1.0));
	printf("%.2lf\n", fabs(-5.0));
	printf("%.2lf\n", ceil(-9.8));
	printf("%.2lf\n", ceil(9.8));
	printf("%.2lf\n", floor(9.2));
	printf("%.2lf\n", floor(-9.2));
	printf("%.2lf\n", pow(2, 3));
//	printf("%.2lf\n", fmod(15, 6)); // nedense hata veriyor.
	printf("%.2lf\n", sin(60 * M_PI / 180));
	printf("%.2lf\n", cos(60 * M_PI / 180));
	printf("%.2lf\n", tan(60 * M_PI / 180));

	/* Standart kutuphanedeki bazi fonksiyonlar */
	printf("%d\n", rand()); // 0-RAND_MAX
	printf("%d\n", 1 + rand() % 6); // rand() % 6, 0 ile 5 arasındadır. 1 ekleyince 1-6 aralığında bir sayı alınır.
	printf("%d\n", rand() % 10 + 14); // 14 ile 23 arasindaki 10 sayidan rastgele birini verir.
	// bazı istatistiki durumlarda 0-1 arasında ondalikli bir rastgele sayiya ihtiyac duyariz. bu durumlarda çıkan sayıyı RAND_MAX'a bölebiliriz ki bunun sonucu her zaman 0-1 arasındadır.
	printf("%f\n", (float) rand() / RAND_MAX); // (float), rand() fonksiyonundan cikan degeri float tipine donusturur.
	printf("\n");
	// srand ile 6 adet rastgele sayi (1-49) yazalim:
	srand(time(NULL));
	for (i = 1; i <= 6; i++) printf("%d. sayi = %d\n", i, rand() % 49 + 1);

	return 0;

}
