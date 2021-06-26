#include <stdio.h>

int kacTaneVar(int [], int, int);

int main(){
    int sayilar[10] = {10, 8, 3, 5, 1, 10, 5, 10, 2, 10};

    printf("Girilen dizide %d tane 5 vardir.\n", kacTaneVar(sayilar, 10, 5));
}

int kacTaneVar(int dizi[], int elemanSayisi, int arananEleman){
    int i;
    int toplam = 0;

    for (i = 0; i < elemanSayisi; i++)
        if (dizi[i] == arananEleman)
            toplam++;

    return toplam;
}
