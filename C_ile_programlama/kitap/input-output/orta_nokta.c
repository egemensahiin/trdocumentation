// iki farklı koordinatın orta noktasini hesaplar

#include <stdio.h>

int main(){

	int x1, x2, y1, y2;
	float xo, yo;

	printf("Ilk nokta icin sırayla X1 ve Y1 degerlerini giriniz: ");
	scanf("%d%d", &x1, &y1);
	printf("Ikinci nokta icin sırayla X2 ve Y2 degerlerini giriniz: ");
	scanf("%d%d", &x2, &y2);

	xo = (x1 + x2) / 2;
	yo = (y1 + y2) / 2;

	printf("      %d + %d      %d\n", x1, x2, (x1 + x2));
	printf("xo = ------- = ----- = %f\n", xo);
	printf("        2        2\n");

	printf("      %d + %d      %d\n", y1, y2, (y1 + y2));
	printf("yo = ------- = ----- = %f\n", yo);
	printf("        2        2\n");

}
