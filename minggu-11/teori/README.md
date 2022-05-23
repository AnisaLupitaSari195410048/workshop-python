# Pertemuan ke - 11
## Tutorial Flaskr
Tutorial akan memandu dalam membuat aplikasi blog dasar yang disebut dengan Flaskr. User dapat mendaftar, login, membuat posting, dan mengedit atau menghapus postingannya. Dan juga dapat mengemas dan menginstal aplikasi di komputer lain. Tutorial ini hanya menggunakan apa yang disediakan oleh Flask dan Python. Kemudian flask fleksibel, karena tidak mengharuskan untuk menggunakan proyek atay tata letak kode tertentu. 

Ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan paket untuk mengatur kode menjadi beberapa modul yang dapat diimpor jika diperlukan, dan tutorial ini juga akan melakukannya.

Direktori proyek akan berisi:

- flaskr/, paket Python yang berisi kode aplikasi dan file Anda.

- tes/, direktori yang berisi modul uji.

- venv/, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.

- File instalasi untuk memberi tahu Python cara menginstal proyek Anda.

- Konfigurasi kontrol versi, seperti git. Anda harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek Anda, berapa pun ukurannya.

-  File proyek lain yang mungkin Anda tambahkan di masa mendatang.

## Pengaturan Aplikasi 

Aplikasi Flask adalah turunan dari kelas Flask. Segala sesuatu aplikasi, seperti konfigurasi dan URL, akan didaftarkan dengan kelas ini. Cara paling mudah untuk membuat aplikasi Flask adalah dengan membuat instance Flask global langsung di bagian atas kode Anda, misal "Hello, World!" contoh lakukan pada halaman sebelumnya. 

Alih-alih membuat instance Flask secara global, Anda akan membuatnya di dalam suatu fungsi. Fungsi ini dikenal sebagai pabrik aplikasi. Setiap konfigurasi, registrasi, dan pengaturan lain yang dibutuhkan aplikasi akan terjadi di dalam fungsi, kemudian aplikasi akan dikembalikan.

## Pabrik Aplikasi 
Buat direktori flaskr dan tambahkan file __init__.py. __init__.py berfungsi ganda, hal ini akan berisi pabrik aplikasi, dan memberitahu Python bahwa direktori flaskr harus diperlakukan sebagai sebuah paket. 
'''
import os

 from flask import Flask


 def create_app(test_config=None):
     # create and configure the app
     app = Flask(__name__, instance_relative_config=True)
     app.config.from_mapping(
         SECRET_KEY='dev',
         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
     )

     if test_config is None:
         # load the instance config, if it exists, when not testing
         app.config.from_pyfile('config.py', silent=True)
     else:
         # load the test config if passed in
         app.config.from_mapping(test_config)

     # ensure the instance folder exists
     try:
         os.makedirs(app.instance_path)
     except OSError:
         pass

     # a simple page that says hello
     @app.route('/hello')
     def hello():
         return 'Hello, World!'

     return app
'''

Create_app adalah fungsi pabrik aplikasi. Anda akan menambahkannya nanti di tutorial, tetapi itu sudah banyak membantu.
- app = Flask(__name__, instance_relative_config=True) membuat instance Flask.
- app.config.from_mapping()menyetel beberapa konfigurasi default yang akan digunakan aplikasi menggunakan:
SECRET_GUY digunakan oleh Flask dan ekstensi untuk menjaga keamanan data.
DATABASE adalah jalur tempat file database SQLite akan disimpan
- app.config.from_pyfile() menimpa konfigurasi default dengan nilai yang diambil dari file config.py di folder instance jika ada.
test_config juga dapat diteruskan ke pabrik, dan akan digunakan sebagai pengganti konfigurasi instans.
- os.makedirs() memastikan bahwa app.instance_path tersedia. 
- @app.route() membuat rute sederhana sehingga Anda dapat melihat aplikasi bekerja sebelum masuk ke tutorial selanjutnya.

## Run the Application
Sekarang dapat menjalankan aplikasi menggunakan perintah flask. Mode pengembangan menampilkan debugger interaktif setiap kali halaman memunculkan pengecualian, dan memulai ulang server setiap kali Anda membuat perubahan pada kode. 

## Tentukan dan Akses Database

Aplikasi akan menggunakan database SQLite untuk menyimpan pengguna dan posting. Python hadir dengan dukungan bawaan untuk SQLite dalam modul sqlite3.
SQLite nyaman karena tidak memerlukan pengaturan server database terpisah dan sudah terintegrasi dengan Python.

## Hubungkan ke Database
Hal pertama yang harus dilakukan ketika bekerja dengan database SQLite dan sebagian besar perpustakaan database Python lainnya adalah membuat koneksi ke database tersebut. Setiap kueri dan operasi dilakukan menggunakan koneksi, yang ditutup setelah pekerjaan selesai.
Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan. Hal itu dibuat di beberapa titik saat menangani permintaan, dan ditutup sebelum respons dikirim. g adalah objek khusus yang unik untuk setiap permintaan. Hal ini digunakan untuk menyimpan data yang mungkin diakses oleh beberapa fungsi selama permintaan. Koneksi disimpan dan digunakan kembali alih-alih membuat koneksi baru jika get_db dipanggil untuk kedua kalinya dalam permintaan yang sama.

## Buat Tabel
Dalam SQLite, data disimpan dalam tabel dan kolom. Hal ini perlu dibuat sebelum Anda dapat menyimpan dan mengambil data. Flaskr akan menyimpan user di tabel pengguna, dan posting di tabel post. DROP TABLE IF EXISTS user;
 DROP TABLE IF EXISTS post;
 
 CREATE TABLE user (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT UNIQUE NOT NULL,
   password TEXT NOT NULL
 );

 CREATE TABLE post (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   author_id INTEGER NOT NULL,
   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   title TEXT NOT NULL,
   body TEXT NOT NULL,
   FOREIGN KEY (author_id) REFERENCES user (id)
 );

 def init_db():
     db = get_db()

     with current_app.open_resource('schema.sql') as f:
         db.executescript(f.read().decode('utf8'))


 @click.command('init-db')
 @with_appcontext
 def init_db_command():
     """Clear the existing data and create new tables."""
     init_db()
     click.echo('Initialized the database.')

open_resource() membuka file relatif terhadap paket flaskr, yang berguna karena Anda tidak perlu tahu di mana lokasi itu saat menerapkan aplikasi nanti. click.command() mendefinisikan perintah baris perintah yang disebut init-db yang memanggil fungsi init_db dan menunjukkan pesan sukses kepada pengguna.

## Daftar dengan Aplikasi 
Fungsi close_db dan init_db_command perlu didaftarkan dengan instance aplikasi. jika tidak, mereka tidak akan digunakan oleh aplikasi. 

app.teardown_appcontext() untuk memberi tahu Flask untuk memanggil fungsi itu saat membersihkan setelah mengembalikan respons.

app.cli.add_command() untuk menambahkan perintah baru yang dapat dipanggil dengan perintah flask.

## Tampilan Pertama: Daftar
Ketika pengguna mengunjungi URL /auth/register, tampilan register akan mengembalikan HTML dengan formulir untuk mereka isi. Ketika mereka mengirimkan formulir, itu akan memvalidasi input mereka dan menampilkan formulir lagi dengan pesan kesalahan atau membuat pengguna baru dan pergi ke halaman login. 

Penjelasan Proyek / Describe the Project

File setup.py menjelaskan proyek Anda dan file-file miliknya.

Instal Proyek / Install the Project

Gunakan pip untuk menginstal proyek Anda di lingkungan virtual.