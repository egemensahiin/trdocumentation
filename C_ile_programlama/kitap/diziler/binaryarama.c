#include <stdio.h>
int ikiliAra(int [], int, int);
int kabarcikSirala(int [], int);
int main(){
    int dizi[10] = {1, 34, 12, 65, 34, 5, 78, 0, 3, 29};
    printf("Dizinin siralanmis halinde 5 sayisi %d. indistedir.", ikiliAra(dizi, 10, 5));
}
int ikiliAra(int dizi[], int n, int aranan){
    int bas = 0;
    int son = n-1;
    int orta;
    kabarcikSirala(dizi, n);
    while (bas <= son){ // kontrol koşulu. bu durumda tüm elemanlar kontrol edilmiş olur.
        orta = (bas + son) / 2; // dizinin baştaki orta indisi
        if (dizi[orta] == aranan) // eğer orta indisteki aranan sayiysa return et
            return orta;
        else if (dizi[orta] > aranan) // aranan sayidan buyukse, aramanin sonunu ortanin bir eksigi yap cunku sirali dizide bundan daha buyuk sayilara bakmaya gerek yok
            son = orta - 1;
        else // benzer sekilde aranan orta nokta aranan sayidan kucukse bundan daha kucuklere bakmaya gerek yok o yuzden baslangici ortanin bir buyugu yap
            bas = orta + 1;
    } // bunu ozyineleme ile de yapmak mumkun aslinda uzerine calis

    return -1; // buraya kadar bir deger return edilememisse bulunamamistir.
}
int kabarcikSirala(int dizi[], int n){
    int i, j;
    int yedek;
    for (i = 0; i < n-1; i++)
        for (j = 0; j < n-1; j++)
            if (dizi[j] > dizi[j+1]){
                yedek = dizi[j];
                dizi[j] = dizi[j+1];
                dizi[j+1] = yedek;
            }
}

