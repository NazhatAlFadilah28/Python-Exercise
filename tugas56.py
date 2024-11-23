print("="*30)
print("MENGHITUNG ANGKA GENAP")
print("="*30)
awal = int(input("Masukan Nilai Awal: "))
akhir = int(input("Masukan Nilai Akhir: "))
genap = []
for i in range (awal, akhir + 1):
    if i%2 == 0:
        genap.append(i)

print("Nilai Genap Nya Adalah\t= ", genap)