#include <stdio.h>

void asalyaz(int a, int b);
int asalbul(int a);

int main(){
	int a, b;
	printf("sirasiyla baslangic ve bitis degerlerini giriniz: ");
	scanf("%d%d", &a, &b);

	printf("----------------\n");

	printf("verilen iki sayi arasindaki asal sayilar: \n");
	asalyaz(a, b);
	return 0;
}

void asalyaz(int a, int b){
	int i;
	for (i = a; i <= b; i++){
		if (asalbul(i) == 1)
			printf("%d\n", i);
	}
}

int asalbul(int a){
	int i;
	if (a == 1)
		return 0;
	for (i = 2; i < a; i++){
		if (a % i == 0)
			return 0;
	}
	return 1;
}
