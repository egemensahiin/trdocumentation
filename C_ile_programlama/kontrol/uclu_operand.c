// not hesaplama ama uclu operand ile
//
#include <stdio.h>

int main(){
	int vize, final;
	float ortalama, gecer = 60.0;

	printf("Vize ve final notunuzu giriniz: ");
	scanf("%d%d", &vize, &final);
	printf("------------------\n");

	ortalama = (0.3 * vize + 0.8 * final) / 1.1;

	printf("Ortalaman: %.2f\n", ortalama);
	ortalama >= 60 ? printf("Tebrikler! Dersi geçtin.\n"): printf("Seneye görüşürüz canım...\n");
	return 0;
}

