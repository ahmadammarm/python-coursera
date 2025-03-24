# tuple dalam python adalah jenis data structure yang mirip dengan list
# tuple dapat diisi dengan berbagai jenis tipe data
# tuple juga mendukung for loop dalam pengoperasiannya
# namun perbedaannya adalah tuple bersifat immutable (tidak bisa diubah)
# tuple didefinisikan dengan menggunakan tanda kurung ().

tuple = (1, 2, 3, 4, 5)
print(tuple)

# dalam tuple, ada beberapa method yang bisa digunakan:
# 1. count()
# 2. index()
# 3. len()
# 4. max()
# 5. min()
# 6. sum()
# 7. sorted()

# 1. count() -> menghitung jumlah data tertentu dalam tuple
tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(tuple.count(1))

# 2. index() -> mencari index dari data tertentu dalam tuple
print(tuple.index(2))

# 3. len() -> menghitung jumlah data dalam tuple
print(len(tuple))

# 4. max() -> mencari data terbesar dalam tuple
print(max(tuple))

# 5. min() -> mencari data terkecil dalam tuple
print(min(tuple))

# 6. sum() -> menjumlahkan semua data dalam tuple
print(sum(tuple))

# 7. sorted() -> mengurutkan data dalam tuple
print(sorted(tuple))


# tuple dengan berbagai jenis tipe data
tuplebaru = (1, 2.5, 'a', True)
print(tuplebaru)
print(type(tuplebaru[3]))
