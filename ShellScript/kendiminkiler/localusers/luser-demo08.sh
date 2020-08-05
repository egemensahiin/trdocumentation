#!/bin/bash

# bu scriptte I/O (input/output) yonlendirmeleri gosterilecek. pipingi daha once gorduk zaten.

# STDOUT'un dosyaya yönlendirilmesi.
FILE="/tmp/data"
head -n1 /etc/passwd > ${FILE}

# STDIN'un programa yonlendirilmesi.
read LINE < ${FILE}
echo "LİNEin icerigi: ${LINE}"

# STDOUT'u dosyaya yonlendirirken dosyanin ustune yazilmasi.
head -n3 /etc/passwd > ${FILE}
echo
echo "${FILE}'in icerigi:"
cat ${FILE}

# STDOUT'u dosyaya yonlendirirken dosyaya eklenmesi.
echo "${RANDOM} ${RANDOM}" >> ${FILE}
echo "${RANDOM} ${RANDOM}" >> ${FILE}
echo
echo "${FILE}'in icerigi:"
cat ${FILE}

# FD 0 ~ STDIN
# FD 1 ~ STDOUT
# FD 2 ~ STDERR

# FD 0 (FD=file descripter) kullanilarak STDIN'un programa yonlendirilmesi.
read LINE 0< ${FILE}
echo
echo "LINEin icerigi ${LINE}"

# FD 1 kullanilarak STDOUT'un dosyaya yonlendirilmesi.
head -n3 /etc/passwd 1> ${FILE}
echo
echo "${FILE}'in icerigi:"
cat ${FILE}

# FD 2 kullanilarak STDERR'un dosyaya yonlendirilmesi.
ERR_FILE="/tmp/data.err"
head -n3 /etc/passwd /fakefile 2> ${ERR_FILE}
echo
echo "${ERR_FILE}'in icerigi:"
cat ${ERR_FILE}

# STDOUR ve STDERR'un dosyaya yonlendirilmesi.
head -n3 /etc/passwd /fakefile &> ${FILE}
echo
echo "${FILE}'in icerigi:"
cat ${FILE}

# STDERR ve STDOUT'un pipe boyunca yonlendirilmesi. normalde STDERR, pipetan iletilmez. & kullanılarak STDERR'u da STDOUTla birlikte iletebiliriz. 
echo
head -n3 /etc/passwd /fakefile |& cat -n 

# STDERR'a cikti gonderilmesi. bu sayede programin exit status 1 durumunda hata mesaji vermesini saglayabiliriz.
echo "Bu bir STDERR" >&2

# STDOUT'un yok sayilmasi. yok sayilacak outputlar ve errorlar /dev/null'a yonlendirilebilir. burada bunlar basitce "yok olur".
echo
echo "STDOUT yok sayiliyor:"
head -n3 /etc/passwd /fakefile > /dev/null

# STDERR'un yok sayilmasi
echo
echo "STDERR yok sayiliyor:"
head -n3 /etc/passwd /fakefile 2> /dev/null

# STDOUT ve STDERR'un yok sayilmasi.
echo
echo "STDOUT ve STDERR yok sayiliyor:"
head -n3 /etc/passwd /fakefile &> /dev/null

# Olusturdugumuz dosyalari silelim. bunun icin de mesela /dev/null konumunu kullanabiliriz.
rm ${FILE} ${ERR_FILE} &> /dev/null
