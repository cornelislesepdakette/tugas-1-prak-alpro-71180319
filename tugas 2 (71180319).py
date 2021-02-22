# cornelis lesepda kette
# 71180319
# Universitas Kristen Duta Wacana
"""
contoh soal:
latihan 3.3 

Buatlah sebuah program yang dapat menampilkan jumlah hari dalam suatu bulan di
tahun 2020. Program meminta pengguna memasukkan nomor bulan (1-12), kemudian program
akan menampilkan jumlah hari pada bulan tersebut.

note:
Lengkapi program tersebut dengan penanganan kesalahan jika pengguna memasukkan input
yang tidak valid.
"""
try:
    bulan = int(input("masukkan bulan (1-12): "))
    if bulan < 1 or bulan > 12:
        print("tidak ada bulan dibawah 1 dan diatas bulan 12")
    elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print("jumlah hari adalah 31 hari")
    elif bulan == 2:
        print("jumlah hari adalah 29 hari")
    else:
        print("jumlah hari adalah 30 hari")
except:
    print("Masukkan bilangan dari 1 sampai 12 bukan kalimat!!")