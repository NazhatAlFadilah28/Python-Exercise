print("="*35)
print("APLIKASI NILAI PESERTA DIDIK BARU")
print("="*35)

nilai = int(input("MASUKAN NILAI SISWA SEKOLAH ASAL: "))

if nilai > 70:
    print("selamat anda di terima")
elif nilai < 60:
    print("anda tidak di terima")
else:
    print("MASUKAN YANG BENAR")