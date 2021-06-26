// Yaricap ve yuksekligi verilen bir koninin hacmini hesaplar
// pi sayisi 3.1419

#include <stdio.h>

int main()
{
	int yukseklik, yaricap;
	float alan, hacim;
	float pi = 3.1419;

	printf("Koninin yuksekligi: ");
	scanf("%d", &yukseklik);
	printf("Koninin taban yaricapi: ");
	scanf("%d", &yaricap);
	alan = pi * (yaricap * yaricap);
	hacim = (alan * yukseklik) / 3;
	printf("-----------------------------\nVerilen koninin hacmi: %.2f\n", hacim);
}
