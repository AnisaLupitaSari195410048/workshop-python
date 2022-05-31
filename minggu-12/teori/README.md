# Pertemuan ke 12
## Struktur Data
- More on Lits

Tipe data yang ada pada daftar memiliki beberapa metode lagi. Berikut adalah semua metode objek daftar:

list.append(x) Tambahkan item ke akhir daftar. Setara dengan a[len(a):] = [x].

list.extend(iterable) Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = iterable.

list.insert(i, x) Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum dimasukkan, jadi a.insert(0, x) sisipan di bagian depan daftar, dan a.insert(len(a), x) setara dengan a.append(x).

list.remove(x) Hapus item pertama dari daftar yang nilainya sama dengan x. Ini menimbulkan ValueError jika tidak ada item seperti itu.

list.pop([ i ]) Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar.

list.clear() Hapus semua item dari daftar.

list.index(x [, start [, end ] ]) Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. 

list.count(x) Kembalikan berapa kali x muncul dalam daftar.

list.sort(*, key=None, reverse=False) Urutkan item dari daftar di tempat.

list.reverse() Balikkan elemen daftar di tempatnya.

list.copy() Kembalikan salinan daftar yang dangkal. 

- Using Lists as Queues

Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("masuk terakhir, keluar pertama"). Untuk menambahkan item ke bagian atas tumpukan, gunakan append() untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit.

- Menggunakan daftar sebagai antrian

Daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

- List Comprehensions

Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi tertentu.

- Nested List Comprehensions

Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi arbitrer, termasuk pemahaman daftar lainnya.

- The del statement

Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya pernyataan del. Ini berbeda dengan metode pop yang mengembalikan nilai. pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menetapkan daftar kosong ke irisan).

- Tuples and Sequences

daftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. Mereka adalah dua contoh tipe data dan urutan. Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan.
pada tupel keluaran selalu diapit tanda kurung, sehingga tupel bersarang diinterpretasikan dengan benar; mereka mungkin dimasukkan dengan atau tanpa tanda kurung di sekitarnya, meskipun seringkali tanda kurung diperlukan (jika tupel adalah bagian dari ekspresi yang lebih besar). Hal ini tidak mungkin untuk menetapkan ke item individu dari tupel, namun dimungkinkan untuk membuat tupel yang berisi objek yang bisa berubah, seperti daftar.

- Sets

Python juga menyertakan tipe data untuk set. Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris.

kurung kurawal atau set() fungsi dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan set() not {}; yang terakhir membuat kamus kosong, struktur data yang akan kita bahas di bagian selanjutnya.

- Dictionaries

Tipe data lain yang berguna yang dibangun ke dalam Python adalah kamus. Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci, yang dapat berupa jenis apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti appends() dan extend().

- Looping Techniques

Saat mengulang kamus, kunci dan nilai yang sesuai dapat diambil secara bersamaan menggunakan metode items(). Saat mengulang melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi enumerate(). Untuk mengulang dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi zip().

 >>> questions = ['name', 'quest', 'favorite color']
 >>> answers = ['lancelot', 'the holy grail', 'blue']
 >>> for q, a in zip(questions, answers):
 ...     print('What is your {0}?  It is {1}.'.format(q, a))
 ...
 ### output
 What is your name?  It is lancelot.
 What is your quest?  It is the holy grail.
 What is your favorite color?  It is blue.

Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi reversed().

- More on Conditions

Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa saja, bukan hanya perbandingan.

Operator perbandingan in dan not in adalah keanggotaan tes yang menentukan apakah suatu nilai ada di (atau tidak) dalam wadah. Operator is dan is not membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik. Perbandingan dapat dirantai. Sebagai contoh, a < b == c menguji apakah a lebih kecil dari b dan juga b sama dengan c.

- Comparing Sequences and Other Types

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. perbandingannya menggunakan urutan leksikografis: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil (lebih kecil). Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual.
Footnotes Bahasa lain dapat mengembalikan objek bermutasi, yang memungkinkan rantai metode, seperti d->insert("a")->remove("b")->sort();.