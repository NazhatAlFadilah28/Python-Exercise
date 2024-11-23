print("="*30)
print(" SENSUS USIA")
print("="*30)

sensus = []

penduduk = int(input("Masukkan jumlah penduduk : "))

for i in range(penduduk):
     sensus.append(float(input(f"Masukkan usia penduduk ke-{i+1} : ")))

total = 0
max1 = max2 = 0
min1 = min2 = 1000 

for jumlah in sensus:
     total += jumlah

     if jumlah > max1:
         max2 = max1
         max1 = jumlah
     elif jumlah > max2:
          max2 = jumlah

     if jumlah < min1:
          min2 = min1
          min1 = jumlah
     elif jumlah < min2:
          min2 = jumlah
rata_rata = jumlah / penduduk

print(f'''
Rata-Rata umur nya adalah     : {rata_rata} Tahun
Umur tertua 1 adalah          : {max1} Tahun
Umur tertua 2 adalah          : {max2} Tahun 

Umur termuda 1 adalah         : {min1} Tahun
Umur termuda 2 adalah         : {min2} Tahun
     ''')