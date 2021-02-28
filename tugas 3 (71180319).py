# cornelis lesepda kette
# 71180319
# Universitas Kristen Duta Wacana
'''
contoh soal:
latihan 4.2 pada moodle
    Buatlah sebuah fungsi yang dapat menentukan apakah minimal dua dari tiga
    parameter yang diberikan memiliki digit paling kanan yang sama. Fungsi tersebut menghasilkan
    nilai True jika memenuhi dan False jika tidak memenuhi. Gunakan fungsi tersebut untuk
    mengecek beberapa test-case berikut ini:
    • Input = 30, 20, 18. Output yang diharapkan = True
    • Input = 145, 5, 100. Output yang diharapkan = True
    • Input = 71, 187, 18. Output yang diharapkan = False
    • Input = 1024, 14, 94. Output yang diharapkan = True
    • Input = 53, 8900, 658. Output yang diharapkan = False
    Ketiga bilangan tersebut diinputkan oleh pengguna, sehingga anda perlu membaca input dari
    pengguna. Fungsi anda harus diberi nama cek_digit_belakang().
    '''

def cek_digit_belakang(a, b, c):
    if (a % 10) == (b % 10) or (b % 10) == (c % 10 ) or (a % 10) == (c % 10):
        return print("TRUE")
    else:
        return print ("FALSE")

angka1 = int(input("masukkan bilangan pertama: "))
angka2 = int(input("masukkan bilangan kedua: "))
angka3 = int(input("masukkan bilangan ketiga: "))
hasil = (cek_digit_belakang(angka1, angka2, angka3))