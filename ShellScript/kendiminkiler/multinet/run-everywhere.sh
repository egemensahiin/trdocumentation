#!/bin/bash
#
# Verilen tum argumanalari SERVERLAR dosyasindaki serverlarda calistirir.
#
# kullanilis fonksiyonu
kullanilis(){
  echo "Kullanilis: $0 [-nsv] [-f DOSYA] KOMUT" >&2
  echo "KOMUT'u tek bir komut olarak tum serverlarda calistirir." >&2
  echo "  -f DOSYA  Server listesi olarak DOSYA'yi kullanir. Default: /vagrant/servers" >&2
  echo "  -n        Dry run modu. Calistirilan KOMUT'u gosterir ve cikis yapar." >&2
  echo "  -s        KOMUT'u alici serverda sudo ile calistirir." >&2
  echo "  -v        Kalabalik mod. KOMUT'u calistirmadan once calistirilan serverı gosterir." >&2
}
# Kullanici kontrolu. Root ise uyar:
if [[ "$UID" -eq 0 ]]
then
  echo "Bu script root olarak veya sudo ile calistirilamaz!" >&2
  kullanilis
  exit 1
fi
# Degiskenleri tanimla
SERVERLAR="/vagrant/servers"
  # Degistirilmek istenirse kolaylikla degistirilebilinmesi icin bu secenegi degisken olarak tanimladik.
  # 2 sn'den fazla yanit alinmazsa sonraki servera geciyor.
SSH_OPT="-o ConnectTimeout=2"
# Opsiyonlar:
while getopts nsvf: OPTION
do
  case ${OPTION} in
    n) DRY_RUN="true" ;;
    s) SUDO_MOD="sudo" ;;
    v) VERBOSE_MOD="true" ;;
    f) SERVERLAR=${OPTARG} ;;
    ?) echo "Gecersiz opsiyon girdiniz!"; kullanilis ;;
  esac
done
# Opsiyonlari komut satiri argumanlarindan kaldir.
shift "$(( OPTIND - 1 ))"
# Syntax kontrolu
if [[ "$#" -lt 1 ]]
then
  echo "Komut girilmedi." >&2
  kullanilis
  exit 1
fi
# Komut satirinda kalan her seyi komut olarak ata.
KOMUT="$@"
# Server listesinin var olup olmadigini kontrol et.
if [[ ! -e "${SERVERLAR}" ]]
then
  echo "$SERVERLAR dosyasi bulunamadi!" >&2
  exit 1
fi
# Cikis durumu tanimlayalim:
EXIT_STAT='0'
# SERVERLAR'ı loopa alalim:
for SERVER in $(cat "${SERVERLAR}")
do
  if [[ "${VERBOSE_MOD}" = 'true' ]]
  then
    echo "${SERVER}:"
  fi
  # Iki defa kullanacagimiz icin degiskene atiyoruz komutun tam halini:
  SSH_KOMUT="ssh ${SSH_OPT} ${SERVER} ${SUDO_MOD} ${KOMUT}"
  # Dry run aciksa komut calistirilmayacak, sadece gosterilecek:
  if [[ "$DRY_RUN" = 'true' ]]
  then
    echo "DRY RUN: ${SSH_KOMUT}"
  else
    $SSH_KOMUT
    # ssh komutunun cikis durumunu kontrol et ve ona gore son cikis durumunu degistir, 0 degilse kullaniciyi uyar.
    SSH_EXIT_STAT="${?}"
    if [[ "$SSH_EXIT_STAT" -ne 0 ]]
    then
      EXIT_STAT=${SSH_EXIT_STAT}
      echo "Komut, ${SERVER} uzerinde calistirilamadi." >&2
    fi
  fi
done
# En son calisan ssh komutunun cikis durumunu ver:
exit "${EXIT_STAT}"
