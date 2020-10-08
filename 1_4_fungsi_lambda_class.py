from classy.opemat import operasi
#Fungsi
def tambah(a,b):
    c = a + b
    return c
print(tambah(3,7))

#lambda (fungsi tak bernama/fungsi 1 baris
tambah = lambda a, b : a+b
print (tambah(3,6))

#class
a = int(input('masukkan angka a'))
b = int(input('masukkan angka b'))
p1 = operasi(a,b)
hasil = p1.penambahan()

print(hasil)

