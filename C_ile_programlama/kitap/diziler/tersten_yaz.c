#include <stdio.h>
int main(){
    int sayilar[5]; /* 5 elemanlı bir tamsayı dizisi */
    int i;
    printf("5 adet sayı giriniz: \n");
    for (i = 0; i < 5; i++)
        scanf("%d", &sayilar[i]);
    printf("Girilen sayilarin sondan basa siralamasi: \n");
    for (i = 4; i >= 0; i--)
        printf("%d\n", sayilar[i]);
    return 0;
}
