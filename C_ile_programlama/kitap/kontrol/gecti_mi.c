// Vize-final notlarina gore gecti mi kaldi mi

#include <stdio.h>

int main(){
	int vize, final;
	float ortalama, gecer = 60.0;

	printf("Vize ve final notunuzu giriniz: ");
	scanf("%d%d", &vize, &final);

	ortalama = (0.3 * vize + 0.8 * final) / 1.1;
	if(ortalama >= gecer){
		printf("------------------\n");
		printf("Ortalaman: %.2f\n", ortalama);
		printf("Tebrikler! Dersi geçtin.\n");
	}
	else{
		printf("------------------\n");
		printf("Ortalaman: %.2f\n", ortalama);
		printf("Seneye görüşürüz canım...\n");
	}
}
