// program çok basit, 100 defa aynı şeyi yazıp çıkıyor.
//
#include <stdio.h>

int main(){

	int sayac = 1;

DONGU:
	printf("Merhaba Dunya!\n");
	sayac++;
	if (sayac <= 100)
		goto DONGU;

	return 0;

}
