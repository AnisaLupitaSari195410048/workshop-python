# Pertemua ke 4
## 6. Modules

Jika keluar dari interpreter Python dan masuk kembali, definisi yang dibuat akan hilang. Oleh karena itu, waktu ingin menulis program yang sedikit lebih panjang, menggunakan editor teks untuk menyiapkan input untuk penerjemah dan menjalankan dengan file tersebut sebagai inputan. Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam interaksi juru bahasa. File-file ini disebut modul. Pengertian modul dapat diimpor ke modul lainnya atau ke modul utama atau yang biasanya disebut kumpulan variabel. Modules adalah file yang berisi definisi dan instruksi Python. Nama file adalah nama modul dengan akhiran .py di akhir. Dalam sebuah modul, nama modul (sebagai string) diberikan sebagai nilai dari variabel global name. contoh fibo.py. 

## Tentang modul
Modul juga dieksekusi jika file dieksekusi sebagai skrip) Setiap modul memiliki tabel simbolnya sendiri, yang digunakan sebagai tabel simbol umum oleh semua fungsi yang didefinisikan dalam modul. Biasanya, tetapi tidak wajib, letakkan semua pernyataan impor di bagian atas modul (atau skrip, dalam hal ini). Ada varian dari pernyataan import yang secara langsung mengimpor nama modul ke dalam tabel simbol modul impor. 

## Mengoperasikan modul sebagai skrip 
 Dengan menambahkan kode di akhir modul, dapat membuat file yang digunakan sebagai skrip serta modul yang dapat diimpor, karena kode mem-parsing perintah baris yang tidak berfungsi. Hanya jika modul dijalankan sebagai file "utama", namun jika modul diimpor, kode ini tidak dapat digunakan Kode ini biasanya digunakan untuk menyediakan antarmuka pengguna yang nyaman bagi modul atau untuk tujuan pengujian.

 ## Pencarian modul waktu modul tidak ditemukan
 Direktori yang berisi skrip input (atau direktori saat ini jika tidak ada file yang ditentukan). Ini berarti bahwa skrip di direktori ini akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan. 

 ## Python "Compiled"
 yaitu untuk percepat proses pemuatan modul, python menyimpan cache dengan versi yang terkompilasi pada setiap modul dari direktori pycache yang bernama module. 

 ## Modul Standar Python
 yaitu memiliki pustaka modul standar, dijelaskan dalam dokumen yang terpisah, pada referensi Pustaka Python. Beberapa modul dibangun ke dalam juru bahasa; ia menyediakan akses ke operasi yang bukan bagian dari bahasa inti tetapi masih terpasang, untuk efisiensi, atau menyediakan akses ke sistem operasi primitif seperti panggilan sistem. 

 ## Fungsi dir() Python 
 yaitu berfungsi untuk mencari tahu nama-nama yang ditentukan oleh modul. dan mengembalikan list string yang telah diurutkan.

 ## Paket 
 Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Ada banyak operasi berbeda yang mungkin ingin kita lakukan pada data audio (seperti pencampuran, penambahan gema, aplikasi fungsi seimbang, membuat efek suara timbul membuat), sehingga akan menulis garis modul yang tidak dapat diandalkan untuk dilakukan Operasi ini.

 ## Impor * Dari Paket
 Pernyataan impor menggunakan konvensi berikut: jika kode __init__.py paket mendefinisikan daftar bernama __all__, itu dianggap sebagai daftar nama modul yang harus diimpor ketika dari paket impor * ditemukan. Terserah pembuat paket untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis. Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat gunanya mengimpor * dari paket mereka. Misalnya, file suara/efek/__init__.py

 ## Intra-package References
 Yaitu menggunakan impor absolut untuk merujuk ke submodul dari paket yang digunakan. contoh, jika modul yang digunakan adalah sound.filters.vocoder, ketika menggunakan modul echo dari paket sound.effects, modul tersebut dapat menggunakan echo import sound.effects sebagai perintahnya.

 ## Packages in Multiple Directories
  paket mendukung satu atribut khusus, path. dapat diinisialisasikan menjadi daftar yang berisi nama direktori yang menyimpan file paket. Variabel dapat dimodifikasi. Serta dapat mempengaruhi pencarian modul dan subpackage di masa depan yang terkandung dalam paket.