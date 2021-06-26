#include <stdio.h>
int main(){
    int n[5] = {13, 12, 0, 5, 8};
    int i,j;
    int yedek;
    printf("Dizinin sirasiz hali: \n");
    for (j = 0; j < 5; j++)
        printf("%d\t", n[j]);

    for (i = 1; i < 5; i++){// i geçişler için. 5 eleman için 4 geçiş yapıyoruz.
        for (j = 0; j < 5-1; j++){ 
            if (n[j] > n[j+1]){
                yedek = n[j];
                n[j] = n[j+1];
                n[j+1] = yedek;
            }
        }
    }
    printf("\nDizinin sıralı hali: \n");
    for (j = 0; j < 5; j++)
        printf("%d \t", n[j]);
    return 0;
}
