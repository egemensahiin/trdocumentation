#include <stdio.h>
int x = 10; /* x değişkeni globaldir ve dosya faaliyet alanına sahiptir. */
void a(void);
void b(void);
void c(void);
int main(){
    int x = 20; /* bu x değişkeni ise lokal bir değişkendir. */
    printf("main blogundaki x = %d\n", x); /* buradan çıktı olarak 20 alınır.
    lokal bir değişken ile global bir değişken aynı isme sahipse, lokal 
    değişken global değişkeni maskeler. */
    { /* yeni bir blok başlattık. bu blok içersindeki her şey, blok faaliyet
         alanına sahiptir. */
        int x = 30;
        printf("main içersindeki blokta x = %d\n", x); /* burdan da yine iç
        bloktaki çıktı alınır. yani x = 30 çıkar. */
    } /* burada blok sonlanır. bundan sonraki faaliyet alanı, main
         fonksiyonuna aittir. */
    printf("bloktan sonra main fonksiyonundaki x = %d\n", x); /* artık blok
    alanından çıktık ve main fonksiyonunun alanına geri döndük. burada
    göreceğimiz x değeri 20 olur çünkü blok içersineki x değeri lokal olduğu
    ve blok faaliyet alanı ile sınırlı olduğu için main fonksiyonu içersinden
    bu değere ulaşılamaz. */
    printf("\n------Fonksiyonlar ilk defa çağırılıyor.------\n");
    a(); /* otomatik ömürlü, yerel bir x değişkeni var. */
    b(); /* durağan ömürlü, yerel bir x değişkeni var.  */
    c(); /* içersinde tanımlanmış bir x değişkeni yok, globaldeki x
    değişkenini kullanıyor. */
    printf("\n----Fonksiyonlar ikinci defa çağırılıyor.----\n");
    a(); /* yerel x'i yeniden oluşturuyor. (otomatik) */ 
    b(); /* yerel x'in son halini kullanıyor. (statik) */
    c(); /* global x'in eski değerini kullanıyor. */
    printf("\nmain içersinde x'in son değeri = %d\n", x);
    return 0;
}
void a(void){
    auto int x = 40; /* fonksiyon her çağırıldığında bu değer atanır. */
    printf("\na fonksiyonunun kapsamındayız. x = %d\n", x);
    ++x;
    printf("hala a'dayız ve x'i 1 arttırdık (++x). şu anda x = %d\n", x);
}
void b(void){
    static int x = 50; /* bu x değişkeni durağan tanımlı, yerel bir değişken.
    ilk çapırıldığında belleğe yerleşir ve bu satırdaki ilk değer atama
    işlemi yalnızca fonksiyon ilk çalıştığında geçerlidir. */
    printf("\nb fonksiyonunun kapsamındayız. x = %d\n", x);
    x = x + 2;
    printf("hala b'deyiz ve x'i 2 arttırdık. şu anda x = %d\n", x);
}
void c(void){
    printf("\nc fonksiyonunun kapsamındayız. x = %d\n", x);
    x = x * 2;
    printf("hala c'deyiz ve x'i 2 ile çarptık. şu anda x = %d\n", x);
}
