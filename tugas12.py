print("="*30)
print("RUMUS DISKON")
print("="*30)

#harga belanjaan konsumen

belanjaan = int(input("MASUKAN HARGA BARANG ANDA : "))

print("="*30)

if belanjaan > 100 :
    print("ANDA MENDAPATKAN DISKON : ",belanjaan / 20 )
else :
    print("ANDA TIDAK MENDAPATKAN DISKON")