print("="*30)
print("MENGHITUNG GANJIL")
print("="*30)

awal = int(input("Masukan Nilai Awal : "))
akhir = int(input("Masukan Nilai Akhir : "))
ganjil = []
for i in range (awal, akhir +1) :
    if i%2 == 1:
        ganjil.append(i)

print("Nilai Ganjil Nya Adalah\t= ", ganjil)