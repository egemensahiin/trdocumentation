#include <stdio.h>

#define M 2
#define N 4

void diziYaz( int a[][N] );

int main(){
    int dizi[M][N] = {{1, 2, 3, 4},
                      {6, 7, 8, 9}};
    printf("dizi'nin bellekteki yeri %p\n", &dizi);
    printf("0-0. indisin bellekteki yeri %p, değeri %d\n", &dizi[0][0], dizi[0][0]);
    printf("0-1. indisin bellekteki yeri %p, değeri %d\n", &dizi[0][1], dizi[0][1]);
    printf("0-2. indisin bellekteki yeri %p, değeri %d\n", &dizi[0][2], dizi[0][2]);
    printf("0-3. indisin bellekteki yeri %p, değeri %d\n", &dizi[0][3], dizi[0][3]);
    printf("1-0. indisin bellekteki yeri %p, değeri %d\n", &dizi[1][0], dizi[1][0]);
    printf("1-1. indisin bellekteki yeri %p, değeri %d\n", &dizi[1][1], dizi[1][1]);
    printf("1-2. indisin bellekteki yeri %p, değeri %d\n", &dizi[1][2], dizi[1][2]);
    printf("1-3. indisin bellekteki yeri %p, değeri %d\n", &dizi[1][3], dizi[1][3]);
    printf("------Diziyi-Yazdiran-Fonksiyon------\n");
    diziYaz(dizi);
    return 0;
}

void diziYaz( int a[][N] ){
    int i, j;

    for(i = 0; i < M; i++){
        printf("%d. satirdaki elemanlar: ", i);
        for(j = 0; j < N; j++)
            printf("%d ", a[i][j]);
        printf("\n");
    }
}
