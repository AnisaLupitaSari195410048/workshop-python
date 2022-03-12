# Pertemuan ke 5
## Input dan Output

Untuk menampilkan output dari suatu program, data cetak dalam bentuk yang dapat dibaca oleh manusia. Ada beberapa cara untuk memformat output :

1. Untuk menggunakan literal string yang diformat, mulai string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, dapat menulis ekspresi Python antara karakter { dan } yang dapat merujuk ke variabel atau nilai literal.
2. Metode string str.format(). Menggunakan { dan } untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi juga harus memberikan informasi yang akan diformat.
3. Dari sini dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pengirisan string dan penggabungan untuk membuat tata letak. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string ke lebar kolom tertentu.

## Fungsi str() 
Fungsi str() yaitu digunakan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr() digunakan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str() akan mengembalikan nilai yang sama dengan repr().

## Literal string yang diformat (f-string)
string yang memungkinkan untuk memasukkan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {expression}. Penggunaan dasar metode str.format() Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke metode str.format(). Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang diteruskan ke metode str.format().

## Pemformatan string lama 
Operator % (modulo) dapat digunakan untuk pemformatan string. Nilai % 'string', instance % dalam string diganti dengan nol atau lebih elemen nilai. Operasi ini umumnya dikenal sebagai interpolasi string

## Membaca dan Menulis File

open() mengembalikan objek file, dan paling sering digunakan dengan dua argumen: open(nama file, mode). Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan.
