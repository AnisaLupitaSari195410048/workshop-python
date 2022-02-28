## Pertemuan ke-3 ##
# Struktur Data
Struktur Data adalah struktur yang dapat menyimpan dan mengorganisasikan kumpulan data. Berikut struktur data yang ada dalam Python.

## List ##
List adalah struktur data yang menyimpan koleksi data terurut, anda dapat menyimpan sequence / rangkaian item menggunakan list. List tipe data memiliki beberapa metode. Berikut ini metode list objek:

1. list.append(x)
menambahkan item ke akhir daftar. 
2. list.extend(iterable)  Perluas daftar dengan menambahkan semua item dari iterable. 
3. list.insert(i, x)  Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya, jadi a.insert(0, x) disisipkan di depan list, dan a.insert(len(a), x) sama dengan a.append( x).
4. list.remove(x) Hapus item pertama dari list yang nilainya sama dengan x. Ini akan menimbulkan ValueError jika tidak ada item seperti itu.
5. list.pop([i])
Hapus item pada posisi yang diberikan dalam list, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam list.
6. list.clear() Hapus semua item dari daftar. 
7. list.count(x)
mengembalikan berapa kali x muncul dalam list.
8. list.sort(*, key=None, reverse=False) mengurutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat diurutkan() untuk penjelasannya).
9. list.reverse()
mengembalikan elemen list ditempatnya.
10. list.copy()
mengembalikan salinan daftar yang dangkal.
11. list.index(x[, start[, end]]) yaitu indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menaikkan ValueError jika tidak ada item seperti itu.

> Lists as Stacks
yaitu method list yang akan mempermudahkan untuk menggunakan list sebagai stack, yang elemen terakhir akan ditambahkan adalah elemen pertama yang diambil. Kemudian menambahkan item ke bagian atas stack, gunakan append(). Lalu mengambil item dari atas stack, gunakan pop() tanpa explicit index.

>Lists as Queues yaitu untuk menggunakan list sebagai antrian, dimana elemen pertama yang ditambah adalah elemen pertama yang diambil.

>List Comprehensions yaitu cara ringkas untuk membuat list. List Comprehensions terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa for, lalu 0(nol) atau lebih klausa for atau if. Hasilnya adalah list baru yang dihasilkan dari evaluasi ekspresi dalam konteks klausa for dan if yang mengikuti. 

>Nested List Comprehensions yaitu ekspresi awal dalam pemahaman daftar dapat berupa ekspresi sembarang,
# 
# Del Statements
Yaitu pernyataan del yang digunakan untuk menghapus item dari list yang diberikan indeksnya alih-alih nilainya.  Pernyataan del juga dapat digunakan untuk menghapus beberapa bagian dari list, atau menghapus seluruh list. 

# Tuples and Sequences
Tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma. Tuple tampak mirip dengan list. Keduanya sering digunakan dalam situasi dan tujuan yang berbeda. Tuple tidak dapat diubah, dan biasanya berisi urutan elemen heterogen yang diakses via unpacked. List bisa berubah, dan elemennya merupakan homogen dan diakses dengan mengulangi list. Tuple mirip dengan list namun tuple bersifat immutable (tidak bisa diubah setelah didefinisikan).
Tuple dibuat dengan menspesifikasikan item tuple dipisahkan menggunakan tanda koma dan opsional diapit dengan tanda kurung. 

# Sets
Python juga menyertakan tipe data untuk set. Sets adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris. 

# Dictionaries
Dictionary seperti buku alamat, dengan buku alamat anda bisa mencari alamat atau detail kontak hanya menggunakan nama orang yang anda cari. Dalam mengasosiasikan key (nama) dengan value (detail). Catatan key harus bersifat unik, anda tidak bisa menemukan informasi yang tepat jika ada dua orang yang mempunyai nama yang sama dalam buku alamat.

# Looping Techniques
Perulangan atau looping adalah sebuah pernyataan dalam bahasa pemrograman dalam mengulang blok kode yang sama berdasarkan dari kondisi atau jumlah data yang didefinisikan.

# More on conditions 
Kondisi dalam pernyataan while dan if dapat berisi operator apa saja, bukan hanya perbandingan. Perbandingan(Comparisons) dapat digabungkan menggunakan Boolean dan or dan hasil perbandingan(ekspresi Boolean) dapat dinegasikan dengan not.

# Comparing Sequences and Other Types
Objek sequences yaitu yang biasanya dapat dibandingkan dengan objek lain dengan jenis sequences yang sama. Perbandingan menggunakan lexicographical ordering: dua item pertama dibandingkan, jika berbeda maka menentukan hasil perbandingan. Jika sama, maka dua item berikutnya dibandingkan, dan seterusnya sampai salah satu sequences habis.
