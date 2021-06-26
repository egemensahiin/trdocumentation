// Iki tamsayinin harmonik ortalamasini hesaplar.
#include <stdio.h>

int main()
{
	int   sayi1;
	int   sayi2;
	float ortalama;

	printf("Iki adet sayi giriniz: ");
	scanf("%d%d", &sayi1, &sayi2);
	ortalama = (2.0 * sayi1 * sayi2) / (sayi2 + sayi1);
	printf("-------------------------\nVerilen sayilarin harmonik ortalamasi: %.2f\n", ortalama);
}
