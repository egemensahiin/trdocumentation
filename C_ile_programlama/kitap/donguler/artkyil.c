// baslangic ve bitis yillari arasindaki artik yillari ve bunlarin sayisini hesaplar.

#include <stdio.h>
int main(){

	int baslangic, bitis;
	int artik = 0;
	int i;

	printf("Baslangic yilini giriniz: ");
	scanf("%d", &baslangic);
	printf("Bitiş yilini giriniz: ");
	scanf("%d", &bitis);

	printf("--------------------------\n");

	for(i = baslangic; i <= bitis; i++){	
		if(i % 4 == 0){
			printf("%d, ", i);
			artik++;
		}
	}

	printf("\nToplamda %d adet artik yil mevcuttur.", artik);

	return 0;

}
