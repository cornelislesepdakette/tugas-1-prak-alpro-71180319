# cornelis lesepda kette
# 71180319

nama = str(input("masukkan nama : "))
jabatan = str(input("masukkan jabatan : "))
tahun_awal = int(input("masukkan tahun awal bekerja : "))
tahun_akhir = int(input("masukkan tahun akhir bekerja : "))
gaji_pokok = int(input("masukkan gaji pokok: "))
jam_kerja = int(input("masukkan jam kerja : "))
hari_kerja = int(input("masukkan hari kerja"))
anak = int(input("masukkan jumlah anak : "))

total_gaji_bulan = (hari_kerja * jam_kerja * gaji_pokok) + (anak * 25000)
total_gaji_pertahun = total_gaji_bulan * 12
total_gaji_seluruh = total_gaji_pertahun * (tahun_akhir-tahun_awal)

print("\n\n output dari inputan diatas")
print("jumlah gaji perbulan : ", total_gaji_bulan)
print("jumlah gaji pertahun : ", total_gaji_pertahun)
print("jumlah gaji seluruh : ", total_gaji_seluruh)