#include <stdio.h>

char harfeCevir(float ortalama){

	if (ortalama < 60)
		return 'F';
	if (ortalama < 70)
		return 'D';
	if (ortalama < 80)
		return 'C';
	if (ortalama < 90)
		return 'B';
	
	return 'A';
}

float ortalamaHesapla(int vize, int final){

	return (0.4 * vize + 0.6 * final);

}

int main(){

	int vize;
	int final;

	printf("Ogrencinin vize notunu giriniz: ");
	scanf("%d", &vize);
	printf("Ogrencinin final notunu giriniz: ");
	scanf("%d", &final);

	printf("Ogrencinin harf notu %c\n", harfeCevir(ortalamaHesapla(vize, final)));

}
