# dalam python juga ada fitur yang dinamakan scope
# scope adalah ruang lingkup sebuah variabel yang bisa diakses oleh program
# ada 4 jenis scope dalam python:
# 1. Local scope
# 2. Enclosing scope
# 3. Global scope
# 4. Built-in scope

# 1. Local scope
# local scope adalah scope yang berada di dalam sebuah fungsi
# variabel yang didefinisikan di dalam fungsi hanya bisa diakses di dalam fungsi tersebut

def my_func():
    x = 10
    print(x)

my_func()

# jika kita mencoba mengakses variabel x di luar fungsi my_func, maka akan terjadi error
# print(x) # NameError: name 'x' is
# not defined

# 2. Enclosing scope
# enclosing scope adalah scope yang berada di dalam fungsi yang lain
# variabel yang didefinisikan di dalam fungsi yang lain, bisa diakses di dalam fungsi yang lain tersebut

def my_func1():
    x = 10
    def my_func2():
        print(x)
    my_func2()

my_func1()

# 3. Global scope
# global scope adalah scope yang berada di luar fungsi
# variabel yang didefinisikan di luar fungsi bisa diakses di dalam fungsi

x = 10
def my_func3():
    print(x)

my_func3()

# 4. Built-in scope
# built-in scope adalah scope yang berada di dalam python
# variabel yang didefinisikan di dalam python bisa diakses di dalam fungsi

def my_func4():
    print(abs(-10))

my_func4()

hasil = 5

def tambah(a, b):
    total = a + b
    print(hasil)
    
    def kali():
        print(total * 2)
    
    kali()

tambah(10, 20)

