# dalam python juga ada struktur data yang bernama dictionary
# dictionary adalah struktur data yang digunakan untuk menyimpan data dalam bentuk key-value pair
# dictionary didefinisikan dengan menggunakan tanda kurung kurawal {}
# dictionary bisa diisi dengan berbagai jenis tipe data
# dictionary bersifat mutable (bisa diubah)

# contoh dictionary
# dictionary kosong
dict1 = {}

# dictionary dengan key-value pair
dict2 = {
    'nama': 'Andi',
    'umur': 21,
    'pekerjaan': 'developer'
}

print(dict2)
# output: {'nama': 'Andi', 'umur': 21, 'pekerjaan': 'developer'}

# dictionary dengan berbagai jenis tipe data
dict3 = {
    'nama': 'Andi',
    'umur': 21,
    'pekerjaan': 'developer',
    'hobi': ['membaca', 'berenang', 'makan'],
    'menikah': False
}

print(dict3)

print(dict3['nama'])

# ada beberapa method yang bisa digunakan untuk memanipulasi dictionary
# 1. clear()
# 2. copy()
# 3. fromkeys()
# 4. get()
# 5. items()
# 6. keys()
# 7. pop()
# 8. popitem()
# 9. setdefault()
# 10. update()
# 11. values() 

# 1. clear() -> menghapus semua data dalam dictionary
dict3.clear()

# 2. copy() -> mengcopy data dalam dictionary
dict3 = {
    'nama': 'Andi',
    'umur': 21,
    'pekerjaan': 'developer',
    'hobi': ['membaca', 'berenang', 'makan'],
    'menikah': False
}

dict3_copy = dict3.copy()
print(dict3_copy)

# 3. fromkeys() -> membuat dictionary baru dengan key tertentu
keys = ['nama', 'umur', 'pekerjaan']
value = 'unknown'

dict4 = dict.fromkeys(keys, value)
print(dict4)

# 4. get() -> mengambil value dari key tertentu
print(dict3.get('nama'))

# 5. items() -> mengambil key-value pair dalam dictionary
print(dict3.items())

# 6. keys() -> mengambil key dalam dictionary
print(dict3.keys())

# 7. pop() -> menghapus key tertentu dalam dictionary
dict3.pop('nama')

# 8. popitem() -> menghapus key-value pair terakhir dalam dictionary
dict3.popitem()

# 9. setdefault() -> mengambil value dari key tertentu, jika key tidak ada maka tambahkan key baru dengan value tertentu
print(dict3.setdefault('nama', 'unknown'))

# 10. update() -> menambahkan key-value pair dari dictionary lain ke dictionary yang sudah ada
dict5 = {
    'nama': 'Andi',
    'umur': 21,
    'pekerjaan': 'developer'
}

dict6 = {
    'hobi': ['membaca', 'berenang', 'makan'],
    'menikah': False
}

dict5.update(dict6)
print(dict5)

# 11. values() -> mengambil value dalam dictionary
print(dict3.values())

