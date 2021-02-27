// ev çizen fonksiyon

#include <stdio.h>

void ucgen(){
	printf("   /\\\n");
	printf("  /  \\\n");
	printf(" /    \\\n");
}

void taban_tavan(){
	printf("--------\n");
}

void govde(){
	printf("|      |\n");
	printf("|      |\n");
	printf("|      |\n");
	printf("|      |\n");
}

int main(){
	// 5 tane ev çizelim:
	int i;
	for (i = 1; i <= 5; i++){
		ucgen();
		taban_tavan();
		govde();
		taban_tavan();
		printf("\n");
	}
	return 0;
}
