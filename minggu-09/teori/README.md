# Pertemuan 9
## Bab 12 Virtual Environments and Packages

### 12.1 Introduction
Python sering menggunakan paket dan modul yang tidak datang sebagai bagian dari pustaka standar. Berarti tidak mungkin bagi satu instalasi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.
Solusi untuk masalah ini adalah membuat virtual environment, sebuah struktur direktori mandiri yang berisi instalasi Python untuk versi tertentu dari Python, serta sejumlah paket tambahan.

### 12.2 Creating Virtual Environments
Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut __venv. venv__ biasanya akan menginstal versi Python terbaru yang dimiliki. Jika kita memiliki beberapa versi Python di sistem, kita dapat memilih versi Python tertentu dengan menjalankan python3 atau versi mana pun yang diinginkan. 

Pada lokasi direktori yang umum dipakai untuk lingkungan virtual adalah .venv. Nama ini membuat direktori biasanya tersembunyi di shell dan dengan demikian terpencil sambil memberikan nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrok dengan berkas definisi variabel lingkungan .env yang didukung beberapa peralatan.

Mengaktifkan lingkungan virtual akan mengubah prompt shell kita untuk menunjukkan lingkungan virtual apa yang digunakan, dan memodifikasi lingkungan sehingga menjalankan python akan membuat kita mendapatkan versi dan instalasi Python tertentu.

### 12.3 Managing Packages with pip
kita dapat menginstal, mengupgrade, dan menghapus paket menggunakan program yang disebut pip. Secara bawaan pip akan menginstal paket dari Python Package Index, <https://pypi.org>. kemudian dapat menelusuri Python Package Index dengan membukanya di peramban atau browser web.

pip memiliki sejumlah sub-perintah: "install", "uninstall", "freeze", dls.

Menginstal versi terbaru dari suatu paket dengan menyebutkan nama suatu paket
```(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3```. 

Menginstal versi spesifik suatu paket dengan memberikan nama paket diikuti dengan == dan nomor versi

```(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0```

kemudian menjalankan kembali perintah ini, pip akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa-apa. Kita dapat memberikan nomor versi yang berbeda untuk mendapatkan versi itu, atau juga dapat menjalankan pip install --upgrade untuk meningkatkan paket ke versi terbaru
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0

pip uninstall diikuti oleh satu atau beberapa nama paket akan menghapus paket-paket dari lingkungan virtual.
pip list akan menampilkan semua paket yang diinstal di lingkungan virtual
```(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)```

pip freeze akan menghasilkan daftar yang sama dari paket yang diinstal, tetapi keluarannya menggunakan format yang diharapkan oleh pip install. Sebuah konvensi yang umum digunakan adalah meletakkan daftar ini dalam file requirements.txt


requirements.txt kemudian dapat dikirimkan atau commit ke sistem kontrol versi dan dikirim sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan install -r
```(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0```