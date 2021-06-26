// program verilen bir sayının palindrom olup olmadığını hesaplar.

#include <stdio.h>

int main(){
	int sayi;
	int birler, onlar, yuzler, binler, onbinler, ters;
	printf("5 basamakli bir tamsayi giriniz: ");
	scanf("%d", &sayi);
	printf("--------------------------\n");
	birler = sayi % 10;
	onlar = (sayi % 100) - birler;
	yuzler = (sayi % 1000) - (onlar + birler);
	binler = (sayi % 10000) - (yuzler + onlar + birler);
	onbinler = (sayi % 100000) - (binler + yuzler + onlar + birler);
	ters = (birler * 10000) + (onlar * 100) + yuzler + (binler / 100) + (onbinler / 10000);
	if(sayi == ters)
		printf("Verilen sayi bir palindromdur.\n");
	else
		printf("Verilen sayi bir palindrom değildir.\n");
}
