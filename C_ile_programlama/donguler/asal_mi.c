// program verilen bir sayinin asal olup olmadigini kontorl ediyor.
// bir sayinin asal olmadiğini ispatlamak, oldugunu ispatlamaktan daha kolay.
// bu sebeple for dongusunde, sayiyi (kendisi - 1)'den 2'ye kadar olan sayilarla
// moduler bolume tabii tutacagiz, herhangi bir sonuc 0 cikarsa sayi asal degil.

#include <stdio.h>

int main(){

	long sayi;
	int test = 1; // default varsayim, sayinin asal oldugu.
	long i; // dongu degiskenimiz.

	printf("Bir sayi giriniz: ");
	scanf("%d", &sayi);

	printf("-----------------\n");

	if(sayi == 1)
		test = 0; // 1'e bölümü test etmiyoruz döngümüzde. o yüzden 1'i
		// kontrol etmemiz lazım
	else{
		for(i = sayi -1; i > 1 && test == 1; i--){
		// "test"i de for döngüsünde kullanıyoruz ki asal olmadığını anladıktan
		// sonra boşa çalışmasın program
			if(sayi % i == 0)
				test = 0;
		}
	}
	
	if(test)
		printf("Yazdığınız sayi asaldir.\n");
	else
		printf("Yazdiginiz sayi asal degildir.\n");

	return 0;

}
