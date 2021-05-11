"""
cornelis  lesepda kette
71180319
Universitas Kristen Duta Wacana

Contoh Soal:

Dodi diberi tugas oleh dosen untuk membuat sebuah program python dengan tipe data set, pada tugas tersebut Dodi disuruh untuk menambahkan data pada variabel nilai
dan setelah data ditambah, semua data yang ada pada variabel nilai dihapus kembali.
"""
#sebelum data ditambah
print("sebelum ditambah")
nilai = set([3,5,1,8,6,7])
print(nilai)
#setelah data ditambah
print("setelah ditambah")
nilai.add(4)
print(nilai)
#setelah data dihapus
print("setelah semua data di hapus")
nilai.clear()
print(nilai)