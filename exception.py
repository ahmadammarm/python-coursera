# dalam python ada 2 jenis tipe error
# 1. SyntaxError
# 2. Exception

# SyntaxError
# SyntaxError adalah error yang terjadi ketika ada kesalahan dalam penulisan syntax python
# contoh SyntaxError:
# if a == 10
#     print(a)
# error di atas terjadi karena tidak ada tanda titik dua (:) setelah kondisi if

# Exception
# Exception adalah error yang terjadi ketika program sedang berjalan (runtime) dan bukan karena kesalahan syntax
# exception biasanya terjadi ketika ada kesalahan dalam logika program atau kesalahan dalam penggunaan fungsi
# exception bisa diatasi dengan error handling menggunakan try-except

# ada beberapa jenis exception dalam python:
# 1. ZeroDivisionError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. KeyError
# 7. FileNotFoundError
# 8. ImportError
# 9. KeyboardInterrupt

# 1. ZeroDivisionError -> terjadi ketika kita mencoba membagi angka dengan 0
# print(10 / 0)

# 2. NameError -> terjadi ketika kita mencoba menggunakan variabel yang belum didefinisikan
# print(a)

# 3. TypeError -> terjadi ketika kita menggunakan operasi yang tidak cocok dengan tipe data
# print('a' + 10)

# 4. ValueError -> terjadi ketika kita menggunakan tipe data yang tidak cocok
# print(int('a'))

# 5. IndexError -> terjadi ketika kita mencoba mengakses index yang tidak ada dalam list
# list = [1, 2, 3, 4, 5]
# print(list[10])

# 6. KeyError -> terjadi ketika kita mencoba mengakses key yang tidak ada dalam dictionary
# dict = {
#     'nama': 'Andi',
#     'umur': 21,
#     'pekerjaan': 'developer'
# }
# print(dict['alamat'])

# 7. FileNotFoundError -> terjadi ketika kita mencoba membuka file yang tidak ada
# file = open('file.txt')

# 8. ImportError -> terjadi ketika kita mencoba mengimport module yang tidak ada
# import modul


# error handling menggunakan try-except (ZeroDivisionError)

def pembagian(a, b):
    try:
        hasil = a / b
        print(hasil)
    except ZeroDivisionError:
        print('Tidak bisa membagi angka dengan 0')
    
pembagian(10, 0)
pembagian(10, 2)

# error handling untuk index error
def index_error():
    list = [1, 2, 3, 4, 5]
    try:
        print(list[10])
    except IndexError:
        print('Index tidak ada dalam list')
        
index_error()

# error handling untuk file not found
def file_not_found():
    try:
        file = open('file.txt')
        print(file.read())
    except FileNotFoundError:
        print('File tidak ditemukan')

file_not_found()
