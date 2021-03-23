#cornelis lesepda kette
#71180319
"Universitas Kristen Duta Wacana"
'''
contoh soal:
Toni ingin membuat program python untuk mengubah huruf pertama yang diinputkan user menjadi huruf besar atau kapital.
bagaimana cara membuat program tersebut dengan metode string pada python?
'''
def sliceindex(x):
    i = 0
    for c in x:
        if c.isalpha():
            i = i +1
            return i
def upperfirst(x):
    i = sliceindex(x)
    return x[:i].upper() + x[i:]
x = str(input("masukkan kalimat: "))
y = upperfirst(x)
print(y)