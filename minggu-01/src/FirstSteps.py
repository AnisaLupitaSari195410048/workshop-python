# Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
#Baris pertama berisi beberapa penugasan: variabel a dan b secara bersamaan mendapatkan nilai baru 0 dan 1.
#Perulangan while dijalankan selama kondisi (di sini: a < 10) tetap benar. 
#Tubuh loop diindentasi: lekukan adalah cara Python mengelompokkan pernyataan.
#Fungsi print() menulis nilai argumen yang diberikan.

i = 256*256
print('The value of i is', i)
The value of i is 65536
#The keyword argument end can be used to avoid the newline after the output, or end the output with a different string

a, b = 0, 1
 while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
#The keyword argument end can be used to avoid the newline after the output, or end the output with a different string