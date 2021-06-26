#include <stdio.h>
int main(){
    int dizi[5] = {13, 12, 0, 5, 8};
    int i, k, m, enKucuk, yedek;
    printf("Dizinin ilk hali: \n");
    for (i = 0; i < 5; i++)
        printf("%d\n", dizi[i]);
    for (k = 0; k < 5-1; k++){
        enKucuk = k;
        for (m = k+1; m < 5; m++){
            if (dizi[m] < dizi[enKucuk])
                enKucuk = m;
        }
        yedek = dizi[k];
        dizi[k] = dizi[enKucuk];
        dizi[enKucuk] = yedek;
    }
    printf("Dizinin yeni hali: \n");
    for (i = 0; i < 5; i++)
        printf("%d\n", dizi[i]);
}

