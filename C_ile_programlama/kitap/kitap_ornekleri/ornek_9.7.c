#include <stdio.h>

float fonksiyon(float x);
float integral(float a, float b);

int main(){
	float a, b;
	
	printf("sirasiyla a ve b degerlerini giriniz: ");
	scanf("%f%f", &a, &b);

	printf("------------------------\n");

	printf("3x^2 + 5x fonksiyonunun %.2f sayisindan %.2f sayisina integrali %.2f\n", a, b, integral(a, b));
}

float fonksiyon(float x){
	return 3 * x * x + 5 * x;
}

float integral(float a, float b){
	float n, h, k, toplam;

	n = 1000;
	h = (b - a) / n;

	toplam = 0;
	for (k = 1; k < n; k++){
		toplam = toplam + fonksiyon(a + k * h);
	}

	return h * (fonksiyon(a) / 2 + toplam + fonksiyon(b) / 2);
}
