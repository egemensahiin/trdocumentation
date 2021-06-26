// Verilen taban ve yukseklik degerlerini kullanarak ucgenin alanini hesaplar.
#include <stdio.h>

int main()
{
	int   taban;
	int   yukseklik;
	float alan;

	printf("Taban degerini giriniz: ");
	scanf("%d", &taban);
	printf("Yukseklik degerini giriniz: ");
	scanf("%d", &yukseklik);
	alan = (taban * yukseklik) / 2 ;
	printf("------------------\nVerilen ucgenin alani: %.2f\n", alan);
}
