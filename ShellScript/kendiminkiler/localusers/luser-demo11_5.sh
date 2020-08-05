#!/bin/bash

# bash'te matematiksel ifadeler, $((ifade)) syntaxı ile okunur ve yazilir. toplama icin + cikarma icin - carpma icin * bölme icinse / kullanilir.
NUM=$(( 1 + 2 )) # "" icerisine de yazilabilir. bosluklar opsiyoneldir.
echo $NUM
NUM=$(( 3 * 4 ))
echo $NUM
NUM=$(( 2 ^ 3 )) # üstel ifadeler icin ^ kullanilir.
echo $NUM
NUM=$(( 8 - 5 ))
echo $NUM
NUM=$(( 6 / 3 ))
echo $NUM
# bash, ondalikli aritmetigi desteklemez. yani ondalikli sonucu olan bir matematiksel islemin sonucu olarak bash, bunun ondaligi atilmis halini (yuvarlanmis degil) verir.
NUM=$(( 6 / 4 )) # 1.5tir fakat bash ondalikli kismi atar ve sonuc olarak 1 verir.
echo $NUM

# scriptlerde matematiksel operasyonlar genellikle dongu kisitlamak gibi kolay halledilebilecek seyler icin kullanilir fakat eger scriptte ondalikli sayilara ihtiyac duyarsak eksternal
# bir program olan bc (basic calculator) programini kullanmamiz gerekir. bc ile ondalikli aritmetik islemler yapabilmek icin mathlib kutuphanesini kullanmamiz gerekir. bu da bc komutunda
# -l opsiyonuyla mumkundur. bc standart input okumaktadir. yani piplinelarda da kullanilabilir. birer ornekla gorelim:
echo '6 / 4' | bc
# bu sekilde mathlib kullanmadan yine 1 sonucunu aliriz. fakat:
echo '6 / 4' | bc -l
# bcyi komut satirindan calistirdigimizda stdin kabul eden ve islemin sonucunu cikti olarak veren bir program baslatir.

# bcnin bir alternatifi ise awk programidir. syntaxı uzun oldugu icin cok tercih edilmese de daha kisa ciktilar verdigi icin bazı scriptlerde kullanilir.
awk 'BEGIN {print 6 / 4}'

# bash'te moduler aritmetik mumkundur. modulo operatoru % isaretidir.
NUM=$(( 6 % 4 ))
echo $NUM

# matematiksel operasyonlar icinde degiskenleri de kullanabiliriz.
ZAR_A='5'
ZAR_B='3'
TOPLAM=$(( ${ZAR_A} + ${ZAR_B} ))
echo $TOPLAM
# syntaxı bu kadar uzatmaya gerek yok matematiksel operasyonlarda sunu yapabiliyoruz:
TOPLAM=$(( ZAR_A + ZAR_B ))
echo $TOPLAM

# bir degiskenin degerini degistirirken ++ fazlaca kullanilan bir syntaxtir. NUM=$((NUM + 1)) ile ayni seyi yapar.
NUM='1'
(( NUM++ )) # bu syntaxla NUM degiskenine, 1 fazlasini atiyoruz. 
echo $NUM

# ayni syntaxi -- seklinde, cikarma islemiyle de uygulayabiliyoruz.
NUM='2'
(( NUM-- )) # bu syntaxla NUM degiskenine, 1 eksigini atiyoruz. 
echo $NUM

# 1den farkli sayilarla +=, -=, *=, /= vb. syntaxlarini kullanabiliriz.
NUM='10'
(( NUM += 5 ))
echo $NUM
NUM='10'
(( NUM -= 5 ))
echo $NUM
NUM='10'
(( NUM *= 5 ))
echo $NUM
NUM='10'
(( NUM /= 5 ))
echo $NUM
NUM='10'
(( NUM %= 3 ))
echo $NUM
NUM='10'
(( NUM ^= 2 ))
echo $NUM

# matematiksel operasyonlar icin gecerli bir syntax daha soz konusudur. let builtin'idir. basitce aciklamak gerekirse let, $(()) ile ayni seydir.
# NUM=$(( 3 + 2 )) yerine:
let NUM='2 + 3' # yazmak da mumkundur.
echo $NUM # veya:
let NUM++
echo $NUM
let NUM+=5
echo $NUM # syntaxlari kullanilabilir.
# let, ustel ifadeler icin ^ degil ** kullanir.
let NUM='5**2'
echo $NUM

# bir baska syntax da expr komutudur. expr komutu kendine verilen ifadeyi isleyim sonucu SDTOUT olarak verir.
expr 2 + 2
# degiskene expr komutu ile atama yapmak icin mathop syntaxi degil komut syntaxi yani $() kullanilmalidir.
NUM=$(expr 5 + 1)
echo $NUM
