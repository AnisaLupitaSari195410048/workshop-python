# Responsi Workshop Python
- Sebelum menampilkan data grafik, maka harus mengimport dataset terlebihdahulu. Untuk memulai pertama yang dilakukan yaitu menginstall library yang digunakan yaitu library pandas dan matplotlib yang dapat menampilkan fungsi grafik yang bisa digunakan untuk melakukan visualisasi data.
Berikut code untuk menginstall:
```python
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

- Kemudian perintah berikutnya yaitu untuk menampilkan dataset yang sudah dicari. Kemudian dipanggil dataset tersebut. Saya menggunakan data data.csv, yang saya dapatkan dari dataset "Go To College Dataset" dan dataset diberi nama yang sama.
```python
df = pd.read_csv('data.csv')
df.head()
```
output:
```python
 	type_school 	school_accreditation 	gender 	interest 	residence 	parent_age 	parent_salary 	house_area 	average_grades 	parent_was_in_college 	in_college
0 	Academic 	A 	Male 	Less Interested 	Urban 	56 	6950000 	83.0 	84.09 	False 	True
1 	Academic 	A 	Male 	Less Interested 	Urban 	57 	4410000 	76.8 	86.91 	False 	True
2 	Academic 	B 	Female 	Very Interested 	Urban 	50 	6500000 	80.6 	87.43 	False 	True
3 	Vocational 	B 	Male 	Very Interested 	Rural 	49 	6600000 	78.2 	82.12 	True 	True
4 	Academic 	A 	Female 	Very Interested 	Urban 	57 	5250000 	75.1 	86.79 	False 	False
```

- Lanjut pada kode untuk menampilkan tampilan info dari dataset.
```python
df.info()
```
output:
```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   type_school            1000 non-null   object 
 1   school_accreditation   1000 non-null   object 
 2   gender                 1000 non-null   object 
 3   interest               1000 non-null   object 
 4   residence              1000 non-null   object 
 5   parent_age             1000 non-null   int64  
 6   parent_salary          1000 non-null   int64  
 7   house_area             1000 non-null   float64
 8   average_grades         1000 non-null   float64
 9   parent_was_in_college  1000 non-null   bool   
 10  in_college             1000 non-null   bool   
dtypes: bool(2), float64(2), int64(2), object(5)
memory usage: 72.4+ KB
```

## Kesimpulan
Python adalah suatu bahasa pemrograman untuk tujuan umum untuk mempermudah penafsiran dan dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991. Python salah satu bahasa pemrograman yang cocok digunakan dalam jenis kepentingan website, pengembangan aplikasi, dan masih banyak kegunaan lainnya.Pada responsi praktikum kali ini dapat disimpulkan bahwa dapat menginstall beberapa dalam Library seperti Seaborn, pandas, numpy, dan juga matplotlib.pyplot yang terdapat banyak fungsi grafik yang bisa digunakan untuk melakukan menampilkan data. Seperti yang sudah saya cantumkan diatas yaitu menampilkan data dari sebuah dataset data.csv dengan menggunakan library pandas dan matplotlib yang bertujuan untuk menampilkan grafik dari data.csv dengan mudah dan itu yang dinamakan visualisasi data. 