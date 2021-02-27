// verilen sayinin sifira gore durumu

#include <stdio.h>

int main(){
	
	int sayi;
	
	printf("Bir sayi giriniz: ");
	scanf("%d", &sayi);

	if(sayi > 0){
		printf("Verilen sayi sifirdan buyuktur.\n");
	}
	else if(sayi < 0){
		printf("Verilen sayi sifirdan kucuktur.\n");
	}
	else{
		printf("Verilen sayi sifirdir.\n");
	}
	
	return 0;

}
