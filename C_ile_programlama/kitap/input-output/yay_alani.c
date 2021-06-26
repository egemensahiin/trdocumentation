// yaricap ve merkez aci degerlerine gore daire yay alani hesaplar
//
#include <stdio.h>
int main(){
	
	int yaricap, aci;
	float alan, pi = 3.14;

	printf("Yaricap: ");
	scanf("%d", &yaricap);
	printf("Aci: ");
	scanf("%d", &aci);
	alan = (pi * (yaricap * yaricap) * aci) / 360;
	printf("-------------------------\nVerilen daire yayinin alani: %.2f\n", alan);
}
