#include <stdio.h>

void baglantiliCagirim(int a[]);
void diziyiDegistir(int a[]);

int main(){
    int dizi[5] = {1, 2, 3, 4, 5};
    int baskadizi[5] = {0, 3, 6, 2, 8};
    printf("dizi'nin bellekteki yeri %p\n", &dizi);
    printf("0. indisin bellekteki yeri %p, değeri %d\n", &dizi[0], dizi[0]);
    printf("1. indisin bellekteki yeri %p, değeri %d\n", &dizi[1], dizi[1]);
    printf("2. indisin bellekteki yeri %p, değeri %d\n", &dizi[2], dizi[2]);
    printf("3. indisin bellekteki yeri %p, değeri %d\n", &dizi[3], dizi[3]);
    printf("4. indisin bellekteki yeri %p, değeri %d\n", &dizi[4], dizi[4]);
    printf("-----Fonksiyondan cagirildiginda:\n");
    baglantiliCagirim(dizi);
    printf("-----Fonksiyondan baska bir dizi cagirildiginda:\n");
    baglantiliCagirim(baskadizi);
    printf("-----Dizinin 3. indisindeki eleman, fonksiyon cagirimiyla degistirildiginde:\n");
    diziyiDegistir(dizi);
    baglantiliCagirim(dizi);
    return 0;
}

void baglantiliCagirim(int a[]){
    printf("dizi'nin bellekteki yeri %p\n", &a);
    printf("0. indisin bellekteki yeri %p, değeri %d\n", &a[0], a[0]);
    printf("1. indisin bellekteki yeri %p, değeri %d\n", &a[1], a[1]);
    printf("2. indisin bellekteki yeri %p, değeri %d\n", &a[2], a[2]);
    printf("3. indisin bellekteki yeri %p, değeri %d\n", &a[3], a[3]);
    printf("4. indisin bellekteki yeri %p, değeri %d\n", &a[4], a[4]);
}

void diziyiDegistir(int a[]){
    a[3] = 45;
}
