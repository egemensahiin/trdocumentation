#include <stdio.h>
#define R 4
#define C 6
int main(){
    int a[R][C];
    int sutun[C] = {0}; // tum sutunlarda ilk toplam degerler 0 olarak atansin
    int i,j;

    for (i = 0; i < R; i++){
        printf("%d. satirdaki elemanlari giriniz: ", i);
        for (j = 0; j < C; j++)
            scanf("%d", &a[i][j]);
    }
    for (i = 0; i < R; i++)
        for (j = 0; j < C; j++)
            sutun[j] = sutun[j] + a[i][j];
    // bu dongunun sonunda sutun dizisi, her bir sutunun toplamini sirayla iceren bir dizi olacak
    printf("---------------\n");
    for (j = 0; j < C; j++)
        printf("%d. sutunun toplami %d\n", j, sutun[j]);
    return 0;
}

