#include <stdio.h>

int obeb(int a, int b);

int main(){
	printf("%d", obeb(192, 72));
	return 0;
}

int obeb(int a, int b){
	if (a % b == 0)
		return b;
	else
		return obeb(b, a % b);
}
