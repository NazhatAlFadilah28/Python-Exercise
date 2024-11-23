print("="*30)
print("JAM BUKA TUTUP TOKO")
print("="*30)

waktu = int(input("JAM TUTUP DAN BUKA TOKO: "))

if waktu > 13:
    print("TUTUP")
elif waktu < 9:
    print("BUKA")