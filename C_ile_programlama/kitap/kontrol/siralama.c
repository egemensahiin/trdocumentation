// Program verilen 3 adet sayıyı sıralar.
//
// Bu program aslında tüm olasılıkları ifli ifadelerle sıralayarak da yazılabilir
// fakat böyle bir yazım ekonomik değildir. Bunun yerine yer değiştirme algoritması
// kullanmak aynı sonucu daha az kodla elde etmemizi sağlar.
// Yer değiştirme algoritmalarında değerler birbirleriyle kıyaslanır ve kıyaslanma
// sonucunda bir değişkendeki değer başka bir değişkene aktarılır. Fakat kullandığımız
// koşullara ve yaptığımız atamalara bağlı olarak veri kaybı yaşama ihtimali vardır.
// Bu sebeple yer değiştirme işleminde bir yedek değişken kullanılır.
//
//	   ___________|1|____________
//    |						    ▼ 
//  sayi1		 sayi2		 yedek
// ( 40 )		( 20 )		(    )
//   ▲           |  ▲         |
//	 |----|2|----|  |---|3|---|
//
// Diyagramda görüldüğü gibi; Önce sayi1 ve 2 kıyaslanır. Eğer sayi1 sayi2'den büyükse,
// sayi1 içersindeki değer, yedek değişkenine atanır. ardından sayi2'deki değer sayi1'e
// atanır. Son olarak da yedek'teki değer sayi2'ye atanarak başta sayi1'in sahip olduğu
// değer sayi2'ye, sayi2'nin sahip olduğu değer ise sayi1'e atanmış olur. Böylece her
// daim, sayi2, sayi1'den büyük olur. Ardından bu koşulu bir de sayi2 ve sayi3 için
// yapmamız lazım.

#include <stdio.h>

int main(){

	int sayi1, sayi2, sayi3, yedek;

	printf("Uc adet sayi giriniz: ");
	scanf("%d%d%d", &sayi1, &sayi2, &sayi3);
	printf("-----------------------------\n");

	if(sayi1 > sayi2){
		yedek = sayi1;
		sayi1 = sayi2;
		sayi2 = yedek;
	}
	if(sayi2 > sayi3){
		yedek = sayi2;
		sayi2 = sayi3;
		sayi3 = yedek;
	}
	// Bu noktada şunu düşünelim; eğer ilk koşul sağlandıysa ilk sayı sayi2, ikinci
	// sayı ise sayi1 olmuştur. sonra sayi2 ve sayi3'ü kıyasladığımızda bunun da doğru
	// olduğunu farzedelim yani İLK sayının üçüncü sayıdan büyük olduğunu düşünelim.
	// Bu sefer de ilk sayı sayi3, üçüncü sayı ise sayi1 oldu. Peki üçüncü ve ikinci
	// sayının kıyaslanması?? Şu an 1. sayımız sayi3'te, 3. sayımız ise sayi1'de.
	// 2. ve 3. sayıları kıyaslamak için TEKRAR sayi1 ve sayi2'yi kıyaslamalıyız.
	// Eğer ilk ve ikinci koşul veya ikisinden biri yanlışsa da halihazırda sayıları
	// kıyaslamış ve sıralamış oluyoruz.
	if(sayi1 > sayi2){
		yedek = sayi1;
		sayi1 = sayi2;
		sayi2 = yedek;
	}

	printf("Verdiginiz sayilarin sıralamasi: %d, %d, %d\n", sayi1, sayi2, sayi3);
	return 0;

}
