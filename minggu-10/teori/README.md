# Pertemuan ke - 10
## Bangun Aplikasi Python dengan CockroachDB dan psycopg2

Tutorial bagaimana membangun aplikasi Python sederhana dengan CockroachDB dan psycopg2.
Step 1. Mulai CockroachDB
Buat cluster gratis tanpa server (beta)
Jika kita belum mempunyai akun, daftar dahulu akun CockroachDB Cloud. Masuk ke akun Cloud CockroachDB kita. Pada halaman Cluster , klik Buat Cluster. Pada halaman Buat kluster Anda , pilih Tanpa Server. Klik create cluster

Buat pengguna SQL

Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default. Klik Buat & simpan kata sandi. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman. Klik next

Dapatkan sertifikat root

Pilih String koneksi umum dari dropdown Pilih opsi. Buka terminal baru di komputer lokal Anda, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud

Dapatkan string koneksi

Buka bagian General connection string , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

Step 2. Dapatkan kode sampel

Cloning repo GitHub kode sampel:

git clone https://github.com/cockroachlabs/hello-world-python-psycopg2 Kode sampel di example.py melakukan hal berikut:
 Membuat accountstabel dan menyisipkan beberapa baris
    Mentransfer dana antara dua akun dalam suatu transaksi
    Hapus akun dari tabel sebelum keluar sehingga Anda dapat menjalankan kembali kode contoh

Step 3. Instal driver psycopg2
agar dapat menginstal psycopg2-binary, jalankan perintah berikut ini:

pip install psycopg2-binary

Step 4. Jalankan kode

Setel DATABASE_URLvariabel lingkungan ke string koneksi ke cluster CockroachDB Cloud Anda: export DATABASE_URL="{connection-string}" Di mana {connection-string}string koneksi yang Anda peroleh dari CockroachDB Cloud Console.
Aplikasi menggunakan string koneksi yang disimpan ke DATABASE_URLvariabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.
run : cd hello-world-python-psycopg2 python example.py