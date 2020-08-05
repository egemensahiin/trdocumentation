#!/bin/bash

# bu scriptte while dongusu kurup sleep ve shift ten bahsedecegiz. sleep komutu, man sayfasinda bahsedildigi sekilde verilen sure boyunca bekler, pek bir sey yapmaz esasinda. dongulerde komut-
# lardan sonra belirli sure beklemek icin vs kullanilabilir. shift komutu ise, pozisyonel parametreleri degistirir. arguman olarak bir sayi (N) kabul eder ve N default olarak birdir. yani
# mesela shift komutunu calistirdigimizda 1. parametre 2., 2. parametre 3. vs vs olur. bunu verlien belli sayida argumanla while dongusu kurmak icin kullanabiliriz cunku shift her calistigin-
# da (N=1 icin) 1 karakter eksilir. yani toplam pozisyonel argumanlari test ettigimizde shift ile en sonunda bunlarin sayisinin (#) en sonunda 0 olmasini saglayabiliriz.

# while syntaxi: while [[KOMUTLAR]]; do KOMUTLAR; done. dongunun ici dogru oldugu muddetce dongu devam eder.

# her seferinde argumanlari bir azaltarak ilk uc argumani yazdiralim
while [[ "${#}" -gt 0 ]] # yani 0dan fazla pozisyonel parametre varsa
do
  echo "Toplam parametre sayisi: ${#}"
  echo "Parametre 1: ${1}"
  echo "Parametre 2: ${2}"
  echo "Parametre 3: ${3}"
  echo
  shift # boylece donguyu kisitliyoruz. aferin bize.
done
