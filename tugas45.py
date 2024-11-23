print("="*30)
print("PROGRAM MENGHITUNG HARI")
print("="*30)

hari_bulan = 30
hari_tahun = 365

hari = int(input('MASUKAN JUMLAH HARI : '))
tahun = int(hari / hari_tahun)
hari = hari % hari_tahun
bulan = int(hari / hari_bulan)
hari = hari % hari_bulan
print (f"HASILNYA : {tahun} YEAR {bulan} BULAN {hari} HARI")