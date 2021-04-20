"""
cornelis lesepda kette
71180319
universitas kristen duta wacana

contoh soal:
	Seorang pemilik pabrik sepatu bernama ronal , pemilik toko tersebut menugaskan staffnya untuk membuat program python untuk menghitung 
    jumlah penjualan bulan Januari, Februari, dan Maret 2021. 
    Sebagai pemilik toko, ronal ingin tahu dibulan mana penjualan tertinggi, karena staffnya kebingungan mengerjakan tugas tersebut jadi staff itu 
    meminta bantuan kita sebagai anak informatika yang handal untuk menyelesaikan tugasnya tersebut.
"""
bulan = {'Januari': 450, 'Februari': 450, 'Maret': 451}
temp = max(bulan['Januari'],bulan['Februari'],bulan['Maret'])
for i in bulan:
    if temp == bulan[i]:
        print("bulan yang memiliki nilai penjualan tertinggi adalah: ", i)

