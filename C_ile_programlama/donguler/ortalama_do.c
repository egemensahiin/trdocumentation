// klavyeden girilen sayilarin ortalamasini hesaplar
#include <stdio.h>
int main(){
    double toplam = 0;
    double sayi, adet = 0;
    double ortalama;
	do{
	    printf("Sayi giriniz (Sonlandirmak icin -1): ");
	    scanf("%lf", &sayi);
	    if(sayi != -1){
	        toplam += sayi;
	        adet++;
	    }
	}while(sayi != -1);
    ortalama = (toplam / adet);
    printf("----------------\n");
    printf("Verilen tum sayilarin ortalamasi: %.2lf\n", ortalama);
    return 0;
}
