"""
cornelis lesepda kette
71180319
universitas kristen duta wacana

contoh soal:
Soni adalah seorang mahasiswa IT di sebuah kampus ternama yang ada di jogja. Dia diberikan tugas dari dosen untuk membuat sebuah program python
untuk mengecek nilai tuple yang diinputkan menggunakan fungsi def cek(Tuple), karena Soni kebingungan maka ia meminta bantuan kita sebagai sesama
anak IT untuk membuat program tersebut.
"""
def cek(Tuple):
    return all(i == Tuple[0] for i in Tuple)
cek_tuple = (2,30,30,30,30,30)
print(cek(cek_tuple))