print("="*30)
print("MENGHITUNG UKURAN SEPATU")
print("="*30)

sepatu = int(input("MASUKAN UKURAN SEPATU : "))

if sepatu > 40 and sepatu <=45:
     print("BESAR")
elif sepatu > 30:
     print("SEDANG")
elif sepatu >= 25:
     print("KECIL")
else:
     print("UKURAN SEPATU SALAH")