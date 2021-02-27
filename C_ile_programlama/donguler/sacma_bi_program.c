// Bu program abcd = a^a + b^b + c^c + d^d kosulunu saglayan 4 basamakli sayilari bulur.

#include <stdio.h>

int main(){

	int a, b, c, d;	
	int aa = 1, bb = 1, cc = 1, dd = 1;
	int i, j;

	printf("Aranan sayilar: ");

	for (i = 1000; i <=9999; i++){

		d = i % 10;
		c = ((i % 100) - d) / 10;
		b = ((i % 1000) - (d + c)) / 100;
		a = ((i % 10000) - (d + c + b)) / 1000;

		// Fonksiyonlarla yapinca buralar daha kolay tabii.
		if (a == 0)
			aa = 0;
		else
			for (j = 1; j <= a; j++)
				aa = aa * a;
		if (b == 0)
			bb = 0;
		else
			for (j = 1; j <= b; j++)
				bb = bb * b;
		if (c == 0)
			cc = 0;
		else
			for (j = 1; j <= c; j++)
				cc = cc * c;
		if (d == 0)
			dd = 0;
		else
			for (j = 1; j <= d; j++)
				dd = dd * d;

		if (aa + bb + cc + dd == i)
			printf("%d", i);

		aa = 1; /* Bunlari unutunca program boka sariyor. */
		bb = 1;
		cc = 1;
		dd = 1;

	}

	printf("\n");

	return 0;

}
