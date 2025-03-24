# dalam python juga ada fitur yang dinamakan file handling
# file handling adalah proses untuk membuka, membaca, menulis, dan menutup file
# ada beberapa mode yang bisa digunakan untuk membuka file:
# - 'r' -> read -> membaca file
# - 'w' -> write -> menulis file
# - 'a' -> append -> menambahkan data ke dalam file
# - 'r+' -> read and write -> membaca dan menulis file
# - 'w+' -> write and read -> menulis dan membaca file
# - 'a+' -> append and read -> menambahkan dan membaca file

# ada beberapa method yang bisa digunakan untuk memanipulasi file
# 1. read() -> membaca file
# 2. write() -> menulis file
# 3. close() -> menutup file
# 4. readlines() -> membaca file per baris
# 5. seek() -> mengubah posisi pointer dalam file
# 6. tell() -> mengetahui posisi pointer dalam file


# kode untuk membuat file
file = open('data.txt', 'w')
file.write('Hello World')
file = open('data.txt', 'w')
input = file.write('Hello There!')
print(input)

# kode untuk membaca file
file = open('data.txt', 'r')
data = file.read()

# kode untuk menutup file
file = open('data.txt', 'r')
file.close()

# untuk readline akan membaca file per baris dan mengembalikan data dalam bentuk string
file = open('data.txt', 'r')
data = file.readline()
print(data)

# untuk readlines akan membaca file per baris dan mengembalikan data dalam bentuk list
file = open('data.txt', 'r')
data = file.readlines()
print(data)

# untuk seek akan mengubah posisi pointer dalam file
file = open('data.txt', 'r')
file.seek(5)




