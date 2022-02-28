for i in range(5):
    print(i)
#the built-in function range() comes in handy

list(range(5, 10))


list(range(0, 10, 3))


list(range(-10, -100, -30))
#range(10) menghasilkan 10 nilai, indeks legal untuk item dengan urutan panjang 10 

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
#Untuk mengulangi indeks dari suatu urutan

range(10)

sum(range(4))  # 0 + 1 + 2 + 3
#fungsi yang mengambil iterable adalah sum() 