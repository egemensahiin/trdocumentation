#include <stdio.h>

int topla(int a, int b){
	return a + b;
}

int main(){
	int a, b;

	printf("İki adet sayi giriniz: ");
	scanf("%d%d",&a,&b);

	printf("Girilen sayilarin toplami %d", topla(a, b));
	return 0;
}
