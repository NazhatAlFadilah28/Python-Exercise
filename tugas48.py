print("="*30)
print("JUMLAH NILAI SISWA")
print("="*30)

karakter = input("MASUKAN NILAI KARAKTER SISWA: ").lower()
Matematika = int(input("MASUKAN NILAI MATEMATIKA SISWA: "))
indo = int(input("MASUKAN NILAI B INDONESIA SISWA: "))
ing = int(input("MASUKAN NILAI B INGGRIS SISWA: "))
if (karakter == 'a' or karakter == 'b') and Matematika >= 60 and indo >= 70 and ing >= 55:
     print ("LULUS")
else:
     print ("TIDAK LULUS")