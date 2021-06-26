#include <stdio.h>

int enKucuk(int [], int);

int main(){
    int sayilar[5] = {13, 12, 0, 5, 8};
    printf("Girilen dizideki en kucuk eleman %d\n", enKucuk(sayilar, 5));
}

int enKucuk(int dizi[], int elemanSayisi){
    int en_kucuk = dizi[0];
    int i;
    for (i = 1; i < elemanSayisi; i++)
        if (en_kucuk > dizi[i])
            en_kucuk = dizi[i];
    return en_kucuk;
}
