#include <stdio.h>

double kuvvet(float agirlik1, float agirlik2, float uzaklik);

int main(){
	float agirlik1, agirlik2;
	float uzaklik;
	printf("Cisimlerin agirliklarini giriniz: ");
	scanf("%f%f", &agirlik1, &agirlik2);
	printf("Aralarindaki uzakligi giriniz: ");
	scanf("%f", &uzaklik);
	printf("---------------------------------------\n");
	printf("Cekim kuvveti %e Newtondur.\n", kuvvet(agirlik1, agirlik2, uzaklik));
	return 0;
}

double kuvvet(float agirlik1, float agirlik2, float uzaklik){
	double sabit = 6.673E-11;
	return  sabit * (agirlik1 * agirlik2) / (uzaklik * uzaklik);
}
