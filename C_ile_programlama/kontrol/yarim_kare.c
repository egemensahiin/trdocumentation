// yarimkare sayi, ortadan ikiye bölünüp iki parçayı toplayınca sayinin karekoku olan sayilar

#include <stdio.h>

int main(){
	int sayi;
	int parca1, parca2;
	int toplam;
	printf("Dort basamakli sayi giriniz: ");
	scanf("%d", &sayi);
	printf("------------------------------\n");

	parca1 = sayi % 100;
	parca2 = (sayi - parca1) / 100;
	toplam = parca1 + parca2;

	if(toplam * toplam == sayi)
		printf("Verilen sayi bir yarimkaredir.\n");
	else
		printf("Verilen sayi bir yarimkare değildir.\n");
	return 0;
}
