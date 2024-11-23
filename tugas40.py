print("="*30)
print("HARGA DISKON")
print("="*30)

total_harga_barang = int(input("MASUKAN TOTAL BELAJAAN: "))

if total_harga_barang >= 20000:
    diskon = (90/100) * total_harga_barang
    total_harga_barang = total_harga_barang - diskon
    print("Total diskon:", diskon)

print("TOTAL HARGA BARANG:",total_harga_barang)
