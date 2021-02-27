// bu programda iki ornek bir arada.
//
#include <stdio.h>
int main(){
	// ilkinde 0-15 arasi sayilarin 10luk, 8lik ve 16lik karsiliklari:
	int i;
	printf("ONLUK\t8'LIK\t16'LIK\n");
	for(i = 0; i <= 15; i++){
		printf("%d\t%o\t%X\n", i, i, i);
	}

	// ikincisinde ise ASCII karsiliklari ve karakter karsiliklari (65-84):
	char j;
	printf("ASCII\tB.CHAR\tK.CHAR\n");
	for(j = 65; j <= 84; j++){
		printf("%d\t%c\t%c\n", j, j, j + 32);
	}

	return 0;
}
