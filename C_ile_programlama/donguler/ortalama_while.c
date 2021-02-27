// klavyeden girilen sayilarin ortalamasini hesaplar
#include <stdio.h>
int main(){
	// değişkenleri notlardaki gibi atadığımızda "ortalama" değerinin virgülden
	// sonrası hep 0 oluyor. değişkenlerin hepsini double olarak atayınca sıkıntı
	// kalkıyor. sebebini çözemedim.
    double toplam = 0;
    double sayi, adet = 0;
    double ortalama;
    printf("Sayi giriniz (Sonlandirmak icin -1): ");
    scanf("%lf", &sayi);
    while(sayi != -1){
        toplam += sayi;
        adet++;
        printf("Sayi giriniz (Sonlandirmak icin -1): ");
        scanf("%lf", &sayi);
    }
    ortalama = (toplam / adet);
    printf("----------------\n");
    printf("Verilen tum sayilarin ortalamasi: %.2lf\n", ortalama);
    return 0;
}
