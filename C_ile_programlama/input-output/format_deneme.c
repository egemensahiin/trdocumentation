#include <stdio.h>

int main()
{
	double x = 3.176;
	float  y = 3.13;
	int    z = 10;
	char   m = 'a';

	printf("Düz double: %lf Düz float: %f\n", x, y);
	printf("Üstel double: %e Üstel float: %e\n", x, y);
	printf("Virgülden önce 8, sonra 3 basamak double: %f\n", y);
	printf("Pozitif önek: %+.2f\n", x);
	printf("Düz tamsayı: %d Düz karakter: %c\n", z, m);
	printf("Hex sisteminde tamsayı: %x Hex sisteminde büyük harfle tamsayı: %X\n", z, z);
	printf("Sekizlik sistemde tam sayı: %o\n", z);
	printf("Önek 0, 10 karakter: %010d\n", z);
}
