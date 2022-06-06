# Pertemuan 13 
## 10 minutes to pandas
### Pandas 
Pandas adalah sebuah library di python yang berlisensi BSD dan open source yang menyediakan struktur data dan analisis data yang mudah digunakan. Pandas digunakan untuk membuat tabel, mengubah dimensi data, mengecek data, dll. Pandas library juga termasuk salah satu library yang paling populer diantara banyak python library, dan sering digunakan karena kemampuannya untuk mengelola data berbentuk tabel. 

### Menginstall Pandas
Pandas default tidak tersedia pada modul standar, pertama kali instalasi python dan diharuskan untuk melakukan instalasi terlebih dahulu sebelum menggunakan. Dan agar dapat menginstall pandas, dengan menjalankan perintah dengan menggunakan pip di cmd Anaconda.
Dengan menggunakan pip: pip install pandas

Dengan menggunakan library Anaconda, kita bisa menginstallnya dengan perintah berikut, conda install pandas.

### Series
Series adalah array berlabel satu dimensi yang mampu menampung semua tipe data (bilangan bulat, string, angka floating point, objek Python, dll.). Label sumbu secara kolektif disebut sebagai indeks. Indeks yang diteruskan adalah daftar label sumbu. Jadi, ini terbagi menjadi beberapa kasus tergantung pada data apa itu : Dari array Jika datandarray, indeks harus sama panjangnya dengan data.
 Metode dasar untuk membuat Seri adalah dengan memanggil:

s = pd.Series(data, index=index)

### Viewing Data 
DataFrame.to_numpy()memberikan representasi NumPy dari data yang mendasarinya. Perhatikan bahwa ini bisa menjadi operasi yang mahal ketika DataFramememiliki kolom dengan tipe data yang berbeda, yang menghasilkan perbedaan mendasar antara pandas dan NumPy: NumPy array memiliki satu dtype untuk seluruh array, sedangkan pandas DataFrames memiliki satu dtype per column. Kemudian dtype numpy dapat menampung semua dtypes di DataFrame. 

### Selection 
Meskipun ekspresi Python / NumPy standar untuk pemilihan dan pengaturan intuitif dan berguna untuk pekerjaan interaktif, untuk kode produksi, kami merekomendasikan metode akses data panda yang dioptimalkan, .at, .iat, .locdan .iloc. 

### Selection by label 
Pandas menyediakan serangkaian metode untuk memiliki pengindeksan berbasis label murni . Ini adalah protokol berbasis inklusi yang ketat. Setiap label yang diminta harus ada dalam indeks, atau a KeyErrorakan dinaikkan. Saat mengiris, baik batas awal DAN batas berhenti disertakan , jika ada dalam indeks. Bilangan bulat adalah label yang valid, tetapi merujuk ke label dan bukan posisi.
Atribut .locadalah metode akses utama. Berikut ini adalah input yang valid:

    Label tunggal, misalnya 5or 'a'(Catatan yang 5diinterpretasikan sebagai label indeks. Penggunaan ini bukan merupakan posisi bilangan bulat di sepanjang indeks.).

    Daftar atau larik label .['a', 'b', 'c']

    Objek irisan dengan label 'a':'f'(Perhatikan bahwa bertentangan dengan irisan Python biasa, awal dan akhir disertakan, saat ada dalam indeks! Lihat Mengiris dengan label .

    Sebuah array boolean.

    A callable, lihat Seleksi Berdasarkan Callable .

### Selection by position
pandas menyediakan serangkaian metode untuk mendapatkan pengindeksan berbasis bilangan bulat murni . Semantik mengikuti pemotongan Python dan NumPy dengan cermat. Ini adalah 0-basedpengindeksan. Saat mengiris, batas awal disertakan , sedangkan batas atas dikecualikan . Mencoba menggunakan non-integer, bahkan label yang validIndexError akan menaikkan . Atribut .ilocadalah metode akses utama. Berikut ini adalah input yang valid:

   - Sebuah bilangan bulat misalnya 5.
-  Daftar atau larik bilangan bulat .[4, 3, 0]
-  Sebuah objek irisan dengan ints 1:7.
- Sebuah array boolean.
- A callable, lihat Seleksi Berdasarkan Callable .

### Boolean indexing
Menggunakan nilai kolom tunggal untuk memilih data:
```
df[df["A"] > 0]
Out[39]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```
Memilih nilai dari DataFrame tempat kondisi boolean terpenuhi:
```python 
df[df > 0]
Out[40]: 
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
```

### Setting


Menyetel kolom baru secara otomatis menyelaraskan data dengan indeks:
```python
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

s1
Out[46]: 
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
df["F"] = s1
```

Menetapkan nilai menurut label:
```
df.at[dates[0], "A"] = 0
```
Menetapkan nilai berdasarkan posisi:
```
df.iat[0, 1] = 0
```
Pengaturan dengan menetapkan dengan array NumPy:
```
df.loc[:, "D"] = np.array([5] * len(df))
```

### Missing Data
Pandas terutama menggunakan nilai np.nanuntuk mewakili data yang hilang. Ini secara default tidak termasuk dalam perhitungan. Lihat bagian Data yang Hilang. 
Pengindeksan ulang memungkinkan Anda untuk mengubah/menambah/menghapus indeks pada sumbu tertentu. Ini mengembalikan salinan data:
```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])

df1.loc[dates[0] : dates[1], "E"] = 1

df1
Out[57]: 
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  NaN  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  NaN
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  NaN
```

Nilai yang dianggap "missing" Karena data datang dalam berbagai bentuk dan bentuk, panda bertujuan untuk fleksibel dalam menangani data yang hilang. Meskipun NaNmerupakan penanda nilai hilang default untuk alasan kecepatan dan kenyamanan komputasi, kita harus dapat dengan mudah mendeteksi nilai ini dengan data dari berbagai jenis: floating point, integer, boolean, dan objek umum. 

### Operasi biner yang fleksibel
Dengan operasi biner antara struktur data panda, ada dua poin penting yang menarik:

   - Perilaku penyiaran antara objek yang lebih tinggi (mis. DataFrame) dan berdimensi lebih rendah (mis. Seri).

   - Data yang hilang dalam perhitungan.

Kami akan mendemonstrasikan bagaimana mengelola masalah ini secara mandiri, meskipun dapat ditangani secara bersamaan.

### Apply

Menerapkan fungsi ke data:
```python
df.apply(np.cumsum)
Out[66]: 
                   A         B         C   D     F
2013-01-01  0.000000  0.000000 -1.509059   5   NaN
2013-01-02  1.212112 -0.173215 -1.389850  10   1.0
2013-01-03  0.350263 -2.277784 -1.884779  15   3.0
2013-01-04  1.071818 -2.984555 -2.924354  20   6.0
2013-01-05  0.646846 -2.417535 -2.648122  25  10.0
2013-01-06 -0.026844 -2.303886 -4.126549  30  15.0

df.apply(lambda x: x.max() - x.min())
Out[67]: 
A    2.073961
B    2.671590
C    1.785291
D    0.000000
F    4.000000
dtype: float64
```

### Metode

Seri dilengkapi dengan sekumpulan metode pemrosesan string dalam str atribut yang memudahkan pengoperasian pada setiap elemen larik, seperti pada cuplikan kode di bawah ini. Perhatikan bahwa pencocokan pola pada strumumnya menggunakan ekspresi reguler secara default (dan dalam beberapa kasus selalu menggunakannya). Lihat lebih lanjut di Metode String Bervektor.
```python
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

s.str.lower()
Out[72]: 
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object
```

### Concat

Pandas juga menyediakan berbagai fasilitas untuk dengan mudah menggabungkan objek Seri dan DataFrame dengan berbagai jenis logika yang ditetapkan untuk indeks dan fungsionalitas aljabar relasional dalam kasus operasi tipe gabungan/gabung.

### Join

Penggabungan gaya SQL. Lihat bagian Penggabungan gaya database .
```python
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

left
Out[79]: 
   key  lval
0  foo     1
1  foo     2

right
Out[80]: 
   key  rval
0  foo     4
1  foo     5

pd.merge(left, right, on="key")
Out[81]: 
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
```

### Grouping

Dengan "mengelompokkan menurut" kami mengacu pada proses yang melibatkan satu atau lebih dari langkah-langkah berikut:

  -  Membagi data menjadi beberapa kelompok berdasarkan beberapa kriteria
  -  Menerapkan fungsi ke setiap grup secara mandiri *Menggabungkan hasil ke dalam struktur data
