// vize final notlarina gore harf notu
//
#include <stdio.h>

int main(){

	int vize, final;
	float ortalama;
	char harf;

	printf("Vize ve final notlarınızı giriniz.");
	scanf("%d%d", &vize, &final);

	ortalama = (0.4 * vize + 0.6 * final);

	printf("------------------\n");

	if(ortalama >= 80)
		harf = 'A';
	else if(ortalama >= 70)
		harf = 'B';
	else if(ortalama >= 60)
		harf = 'C';
	else if(ortalama >= 50)
		harf = 'D';
	else
		harf = 'F';

	printf("Ogrencinin ortalaması: %.2f\n", ortalama);
	printf("Buna karsilik gelen harf notu: %c\n", harf);
	
	return 0;

}
