# Pertemuan 14
## Scikit-learn
Sklearn merupakan sebuah module dari bahasa pemrograman Python yang dibangun berdasarkan NumPy, SciPy, dan Matplotlib. Fungsi dari module adalah untuk membantu melakukan processing data ataupun melakukan training data untuk kebutuhan machine learnng atau data science. 

### Installing scikit-learn 
Ada beberapa cara untuk menginstal scikit-learn:

    Instal rilis resmi terbaru
-  Ini adalah pendekatan terbaik untuk sebagian besar pengguna. Ini akan memberikan versi stabil dan paket pra-bangun tersedia untuk sebagian besar platform.
  -  Instal versi scikit-learn yang disediakan oleh sistem operasi Anda atau distribusi Python. Ini adalah opsi cepat bagi mereka yang memiliki sistem operasi atau distribusi Python yang mendistribusikan scikit-learn. Ini mungkin tidak menyediakan versi rilis terbaru.
-  Membangun paket dari sumber. Ini adalah yang terbaik untuk pengguna yang menginginkan fitur terbaru dan terbaik dan tidak takut menjalankan kode baru. Ini juga diperlukan untuk pengguna yang ingin berkontribusi pada proyek.

Instal conda menggunakan penginstal Anaconda atau miniconda atau penginstal miniforge (tidak diperlukan izin administrator untuk semua itu).

### An introduction to machine learning with scikit-learn
Secara umum, masalah pembelajaran mempertimbangkan satu set n sampel data dan kemudian mencoba memprediksi sifat data yang tidak diketahui. Jika setiap sampel lebih dari satu angka.

### Loading an example dataset

scikit-learn dilengkapi dengan beberapa kumpulan data standar, misalnya kumpulan data iris dan angka untuk klasifikasi dan kumpulan data diabetes untuk regresi.

Berikut ini, kami memulai interpreter Python dari shell kami dan kemudian memuat irisdan digitsset data. Konvensi notasi kami adalah yang $menunjukkan prompt shell sementara >>> menunjukkan prompt juru bahasa Python:
```python
$ python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
```

### Bentuk Array data
Data selalu berupa larik 2D, bentuk , meskipun data asli mungkin memiliki bentuk yang berbeda. Dalam hal digit, setiap sampel asli adalah gambar bentuk dan dapat diakses menggunakan: (n_samples, n_features)(8, 8).
```python
>>> digits.images[0]
array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.],
       [  0.,   0.,  13.,  15.,  10.,  15.,   5.,   0.],
       [  0.,   3.,  15.,   2.,   0.,  11.,   8.,   0.],
       [  0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.],
       [  0.,   5.,   8.,   0.,   0.,   9.,   8.,   0.],
       [  0.,   4.,  11.,   0.,   1.,  12.,   7.,   0.],
       [  0.,   2.,  14.,   5.,  10.,  12.,   0.,   0.],
       [  0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])
```

### Learning and predicting

Dalam kasus kumpulan data digit, tugasnya adalah memprediksi, dengan diberikan gambar, digit mana yang diwakilinya. Kami diberikan sampel dari masing-masing 10 kelas yang mungkin (angka nol sampai sembilan) yang kami sesuaikan dengan estimator untuk dapat memprediksi kelas yang termasuk dalam sampel tak terlihat.

Dalam scikit-learn, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode dan .fit(X, y)predict(T).

### Conventions

scikit-learn estimator mengikuti aturan tertentu untuk membuat perilaku mereka lebih prediktif. Pada predict() mengembalikan array integer, karena iris.target (array integer) digunakan dalam fit. Yang kedua predict() mengembalikan array string, karena iris.target_names untuk pemasangan. 

### Multiclass vs. multilabel fitting
tugas pembelajaran dan prediksi yang dilakukan bergantung pada format data target yang sesuai dengan:multiclass classifiers. 
```python
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
```

