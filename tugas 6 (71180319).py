"""
cornelis lesepda kette
71180319
universitas kristen duta wacana

contoh soal:
Toto ingin membuat sebuah program menentukan status seseorang berdasarkan umurnya menggunakan percabangan kompleks. Dengan ketentuan:
-dibawah 20 tahun = masih sekolah
-diatas 20 atau di bawah 25 = sudah bekerja
- diatas 25 atau dibawah 30 = sudah menikah
- diatas 30 = sudah punya anak
Bagaimana caranya Toto membuat program tersebut di python?  
"""
var_umur = input("masukkan umur: ")
if (int(var_umur) <25):
    if(int(var_umur) < 20):
        print("anda masih sekolah")
    else:
        print("anda sudah bekerja")
elif (int(var_umur) > 25):
    if(int(var_umur) <30):
        print("anda sudah menikah")
    else:
        print("anda sudah mempunyai anak")
else:
    print("anda sudah menikah")