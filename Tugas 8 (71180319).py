"""
cornelis lesepda kette
71180319
universitas kristen duta wacana

contoh soal:
Dony ini membuat sebuah program untuk bisa menulis atau menyisipkan teks pada file,namun teks tersebut itu harus diinputkan oleh user.
jadi doni meminta bantuan kita sebagai anak informatika untuk membuat program tersebut.
"""
print("=======Selamat datang di program biodata=======")
nama = input("Nama: ")
umur = int(input("Umur: "))
alamat = input("Alamat: ")

teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n".format(nama, umur, alamat)
file_open = open("biodata.txt", "a")
file_open.write(teks)
file_open.close()