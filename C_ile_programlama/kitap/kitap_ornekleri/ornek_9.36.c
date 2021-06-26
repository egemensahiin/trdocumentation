#include <stdio.h>

int faktoriyel(int a);
float kombinasyon(int a, int b);

int main(){
	int a, b;

	printf("Kombinasyonu alinacak sayilari sirasiyla giriniz: ");
	scanf("%d%d", &a, &b);
	printf("-----------------\nC(%d,%d) = %.2f\n", a, b, kombinasyon(a, b));
	return 0;
}

int faktoriyel(int a){
	long int faktoriyel = 1;
	int i;

	if (a == 1)
		return faktoriyel;
	else{
		for (i = 1; i <= a; i++)
			faktoriyel = faktoriyel * i;
	}

	return faktoriyel;
}

float kombinasyon(int a, int b){
	return (faktoriyel(a) / (faktoriyel(a-b) * faktoriyel(b)));
}
