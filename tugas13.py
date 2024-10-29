print("="*30)
print("MESIN KASIR WARUNG MADURA")
print("="*30)

Barang = []
Sabun = [5000]
Susu = [7000]
Handuk = [10_000]

print('''
                Barang Yang Tersedia
|1. Sabun       Rp.5000
|2. Susu        Rp.7000
|3. Handuk      Rp.10.000 
|4. Odol        Rp.
|5. Sikat WC    Rp.
|6. Aqua        Rp.
''')

jumlah = int(input("Masukkan Jumlah Barang Yang Ingin Di Beli : "))
 
def beli():
    for i in range(jumlah):
       kode = int(input(f" NO BARANG {i+1} :"))
    if kode == 1:
       j = int(input(f"Masukkan jumlah yang ingin di beli, barang {kode} : "))
       beli1 = Sabun * j
       Barang.append(beli1)

beli()
    

    