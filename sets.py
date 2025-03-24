# sets dalam python adalah jenis data structure yang mirip dengan list
# sets dapat diisi dengan berbagai jenis tipe data
# sets juga mendukung for loop dalam pengoperasiannya
# namun perbedaannya adalah sets bersifat unordered (tidak memiliki index)
# sets didefinisikan dengan menggunakan tanda kurung kurawal {}
# sets tidak bisa memiliki data yang sama
# jika ada data yang sama, maka data tersebut akan dianggap hanya 1 data

# ada beberapa method yang bisa digunakan untuk memanipulasi sets
# 1. add()
# 2. clear()
# 3. copy()
# 4. difference()
# 5. difference_update()
# 6. discard()
# 7. intersection()
# 8. intersection_update()
# 9. isdisjoint()
# 10. issubset()
# 11. issuperset()
# 12. pop()
# 13. remove()
# 14. symmetric_difference()
# 15. symmetric_difference_update()
# 16. union()
# 17. update()

# 1. add() -> menambahkan data ke dalam sets
sets = {1, 2, 3, 4, 5}
sets.add(6)
print(sets)

# 2. clear() -> menghapus semua data dalam sets
sets.clear()
print(sets)

# 3. copy() -> mengcopy data dalam sets
sets = {1, 2, 3, 4, 5}
sets_copy = sets.copy()
print(sets_copy)

# 4. difference() -> mencari data yang berbeda antara 2 sets
sets1 = {1, 2, 3, 4, 5}
sets2 = {4, 5, 6, 7, 8}
print(sets1.difference(sets2))

# 5. difference_update() -> menghapus data yang sama antara 2 sets
sets1.difference_update(sets2)
print(sets1)

# 6. discard() -> menghapus data tertentu dalam sets
sets = {1, 2, 3, 4, 5}
sets.discard(1)

# 7. intersection() -> mencari data yang sama antara 2 sets
sets1 = {1, 2, 3, 4, 5}
sets2 = {4, 5, 6, 7, 8}
print(sets1.intersection(sets2))

# 8. intersection_update() -> menghapus data yang tidak sama antara 2 sets
sets1.intersection_update(sets2)
print(sets1)

# 9. isdisjoint() -> mengecek apakah 2 sets tidak memiliki data yang sama   
sets1 = {1, 2, 3, 4, 5}
sets2 = {6, 7, 8, 9, 10}
print(sets1.isdisjoint(sets2))

# 10. issubset() -> mengecek apakah sets1 adalah subset dari sets2
sets1 = {1, 2, 3}
sets2 = {1, 2, 3, 4, 5}
print(sets1.issubset(sets2))

# 11. issuperset() -> mengecek apakah sets1 adalah superset dari sets2
sets1 = {1, 2, 3, 4, 5}
sets2 = {1, 2, 3}

print(sets1.issuperset(sets2))

# 12. pop() -> menghapus data secara acak dalam sets
sets = {1, 2, 3, 4, 5}
sets.pop()
print(sets)

# 13. remove() -> menghapus data tertentu dalam sets
sets = {1, 2, 3, 4, 5}
sets.remove(1)

# 14. symmetric_difference() -> mencari data yang berbeda antara 2 sets
sets1 = {1, 2, 3, 4, 5}
sets2 = {4, 5, 6, 7, 8}
print(sets1.symmetric_difference(sets2))

# 15. symmetric_difference_update() -> menghapus data yang sama antara 2 sets
sets1.symmetric_difference_update(sets2)
print(sets1)

# 16. union() -> menggabungkan 2 sets
sets1 = {1, 2, 3, 4, 5}
sets2 = {4, 5, 6, 7, 8}

print(sets1.union(sets2))

# 17. update() -> menambahkan data dari sets lain ke sets yang sudah ada

sets1.update(sets2)
print(sets1)
# output
# {1, 2, 3, 4, 5, 6}