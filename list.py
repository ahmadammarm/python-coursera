# list dalam python adalah struktur data yang digunakan untuk menyimpan data
# list adalah jenis data structure yang paling sering digunakan dalam python
# list bisa menyimpan data dengan berbagai jenis (integer, float, string, dll)
# data dalam list bisa diubah (mutable) dan bisa diakses dengan menggunakan index
# list bisa dibuat dengan menggunakan method list() atau dengan menggunakan tanda kurung []
# list juga mendukung penggunaan for loop dalam pengoperasiannya

list = [1, 2, 3, 4, 5]
print(list)

# operator * sebelum list akan menghasilkan data yang ada di dalam list
list2 = ['a', 'b', 'c', 'd', 'e']
print(*list2)

# ada beberapa method yang bisa digunakan untuk memanipulasi list
# 1. append()
# 2. clear()
# 3. copy()
# 4. count()
# 5. extend()
# 6. index()
# 7. insert()
# 8. pop()
# 9. remove()
# 10. reverse()
# 11. sort()

# 1. append() -> menambahkan data di akhir list
list.append(6)
print(list)

# 2. clear() -> menghapus semua data dalam list
list.clear()
print(list)

# 3. copy() -> mengcopy data dalam list
list = [1, 2, 3, 4, 5]
list_copy = list.copy()
print(list_copy)

# 4. count() -> menghitung jumlah data tertentu dalam list
list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(list.count(1))

# 5. extend() -> menambahkan data dari list lain ke list yang sudah ada
list2 = ['a', 'b', 'c', 'd', 'e']
list.extend(list2)
print(list)

# 6. index() -> mencari index dari data tertentu dalam list
print(list.index('a'))

# 7. insert() -> menambahkan data di index tertentu dalam list
list.insert(0, 'z')
print(list)

# 8. pop() -> menghapus data di index tertentu dalam list
list.pop(0)
print(list)

# 9. remove() -> menghapus data tertentu dalam list
list.remove('z')
print(list)

# 10. reverse() -> membalikkan data dalam list
list.reverse()

# 11. sort() -> mengurutkan data dalam list
list.sort()

# list comprehension adalah cara untuk membuat list dengan menggunakan satu baris kode
# list comprehension bisa digunakan untuk membuat list baru dari list yang sudah ada
# list comprehension bisa digunakan untuk membuat list dengan kondisi tertentu
# list comprehension bisa digunakan untuk membuat list dari string
# list comprehension bisa digunakan untuk membuat list dari tuple
# list comprehension bisa digunakan untuk membuat list dari dictionary

# contoh list comprehension
list = [i for i in range(10)]
print(list)


nama = "Ahmad Ammar Musyaffa"
jumlah_a = nama.count("a")
jumlah_A = nama.count("A")

jumlahHurufA = jumlah_a + jumlah_A

print(jumlahHurufA)

