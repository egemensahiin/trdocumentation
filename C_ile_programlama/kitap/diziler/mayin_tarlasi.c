#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define M 5
#define N 6
#define MAYIN 10

void mayinlari_yerlestir(int [][N]);

int main(){
    int tarla[M][N] = {0};
    int i, j;

    srand(time(NULL));
    mayinlari_yerlestir(tarla);

    for(i = 0; i < M; i++){
        for(j = 0; j < N; j++)
            printf("%d", tarla[i][j]);
        printf("\n");
    }
}

void mayinlari_yerlestir(int a[][N]){
    int i;
    int m, n;

    for(i = 0; i < MAYIN; i++){
        m = rand() % M;
        n = rand() % N;
        if(a[m][n] == 0)
            a[m][n] = 1;
        else
            i--; // eger zaten mayin varsa dongu eksik olmasin
    }
}
