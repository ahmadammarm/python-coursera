# dalam python ada juga fitur yang bernama args dan kwargs
# args adalah singkatan dari arguments dan kwargs adalah singkatan dari keyword arguments

# args adalah parameter yang digunakan untuk mengirim data ke dalam sebuah fungsi dalam bentuk tuple
# kwargs adalah parameter yang digunakan untuk mengirim data ke dalam sebuah fungsi dalam bentuk dictionary

# contoh penggunaan args
def print_data(*args):
    for data in args:
        print(data)

print_data(1, 2, 3, 4, 5)
print_data('a', 'b', 'c', 'd', 'e')

def tambah(*args):
    total = 0
    for data in args:
        total += data
    return total

print(tambah(1, 2, 3, 4, 5))

# cpntoh penggunaan kwargs
def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

nums = 4
for i in nums:
    print(i)