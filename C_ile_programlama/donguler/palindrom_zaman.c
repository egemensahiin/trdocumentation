#include <stdio.h>

int main(){

	int saat, dakika;
	int saatOn, saatBir;
	int dakikaOn, dakikaBir;

	printf("Palindrom zamanlar:\n");

	for(saat = 0; saat < 24; saat++){
		saatBir = saat % 10;
		saatOn  = saat / 10;
		for(dakika = 0; dakika < 60; dakika++){
			dakikaBir = dakika % 10;
			dakikaOn  = dakika / 10;
			if(saatOn == dakikaBir && saatBir == dakikaOn)
				printf("%d%d:%d%d\n", saatOn, saatBir, dakikaOn, dakikaBir);
		}
	}

}
