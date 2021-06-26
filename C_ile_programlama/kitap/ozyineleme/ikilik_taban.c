#include <stdio.h>

int ikilikYaz(int sayi);

int main(){
	printf("%d", ikilikYaz(13));
	return 0;
}

int ikilikYaz(int sayi){
	if (sayi == 1 || sayi == 0)
		return sayi;
	else
		printf("%d", sayi % 2);
		return ikilikYaz(sayi / 2);
}
