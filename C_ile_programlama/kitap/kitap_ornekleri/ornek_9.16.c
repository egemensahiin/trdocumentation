#include <stdio.h>

float yardMetreCevir(float a, char t);

int main(){
	printf("%.4f", yardMetreCevir(3, 'y'));
	return 0;
}

float yardMetreCevir(float a, char t){
	switch (t){
		case 'y':
		case 'Y':
			return a * 0.9144;
			break;
		case 'm':
		case 'M':
			return a / 0.9144;
			break;
		default:
			return 0;
			break;
	}
}
