#include <stdio.h>

void tekMiCiftMi(int sayi){
	if (sayi % 2 == 0)
		printf("Verilen sayi cifttir.");
	else
		printf("Verilen sayi tektir.");
}

int main(){
	int sayi;
	printf("Sayi giriniz: ");
	scanf("%d", &sayi);
	tekMiCiftMi(sayi);
	return 0;
}
