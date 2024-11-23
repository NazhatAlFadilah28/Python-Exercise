print("="*30)
print("HARGA PARKIR")
print("="*30)

jamMasuk = int(input("MASUKAN JAM MASUK (1-12): "))
jamPulang = int(input("MASUKAN JAM PULANG (1-12): "))

if jamMasuk > 12:
    print("Kamu tidak boleh memasukan angka lebih dari 12")
elif jamMasuk < 1:
    print("Kamu tidak boleh memasukan angka kurang dari 1!")

if jamPulang > 12:
    print("Kamu tidak boleh memasukan angka lebih dari 12")
elif jamPulang < 1:
    print("Kamu tidak boleh memasukan angka kurang dari 1!")

if jamMasuk > jamPulang:
    jamKerja = (jamPulang + 12) - jamMasuk

elif jamMasuk <= jamPulang:
    jamKerja = jamPulang - jamMasuk

if jamKerja > 2:
    biayaParkir = 3000 + (500 * jamKerja) - 2000
elif jamKerja <= 2:
    biayaParkir = 3000

print("LAMA KERJA:", jamKerja, "jam")
print("BIYAYA PARKIR:", biayaParkir)