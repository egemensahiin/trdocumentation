#include <stdio.h>

long f(int a);

int main(){
	printf("%ld\n", f(0));
	printf("%ld\n", f(1));
	printf("%ld\n", f(2));
	printf("%ld\n", f(3));
	printf("%ld\n", f(4));
	printf("%ld\n", f(5));
	printf("%ld\n", f(6));
	printf("%ld\n", f(7));
	printf("%ld\n", f(8));
	printf("%ld\n", f(9));
	printf("%ld\n", f(10));
	printf("%ld\n", f(11));
	printf("%ld\n", f(12));
}

long f(int a){
    if (a == 0 || a == 1)
        return a;
    else
        return f(a - 1) + f(a - 2);
}
