print("="*30)
print("MENGHITUNG NILAI TERBESAR TERKECIL")
print("="*30)

nilai1 = int(input("Masukan Nilai 1: "))
nilai2 = int(input("Masukan Nilai 2: "))
nilai3 = int(input("Masukan Nilai 3: "))

maks = 0
if nilai1 > nilai2 :
    maks = nilai1
else :
    maks = nilai2
if nilai3 > maks :
    maks = nilai3

min = 0
if nilai1 < nilai2 :
    min = nilai1
else :
    min = nilai2
if nilai3 < maks :
    min = nilai3

print("Nilai Terbesar Nya Adalah\t=", maks)
print("Nilai Terkecil Nya Adalah\t=", min)