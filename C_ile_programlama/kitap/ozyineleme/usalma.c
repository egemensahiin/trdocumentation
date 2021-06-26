#include <stdio.h>

long usAlma(int taban, int us);

int main(){
	printf("%ld", usAlma(2, 3));
	return 0;
}

long usAlma(int taban, int us){
	if (us == 0)
		return 1;
	else
		return taban * usAlma(taban, us - 1);
}
