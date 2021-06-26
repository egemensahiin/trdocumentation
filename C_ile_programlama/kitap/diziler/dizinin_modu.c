#include <stdio.h>

int mod(int [], int n);

int main(){
    int dizi[10] = {10, 2, 3, 4, 1, 1, 67, 23, 1, 3};
    printf("Girilen dizinin modu: %d", mod(dizi, 10));
    return 0;
}

int mod(int dizi[], int n){
    int frekans[101] = {0}; // her indisten kaç adet oldugunu tutan dizi. ilk degerleri hepsinin 0
    int m;
    int enBuyuk;

    for (m = 0; m < n; m++)
        frekans[dizi[m]]++; // dizinin m'inci elemani icin, 101 elemanli dizinin dizi[m]'inci elemanini 1 arttir.

    enBuyuk = 0;
    for (m = 0; m < 101; m++)
        if (frekans[m] > frekans[enBuyuk])
            enBuyuk = m;
    return enBuyuk;
}
