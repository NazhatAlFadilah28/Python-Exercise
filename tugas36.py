print("="*30)
print("NILAI AKHIR SEMESTER")
print("="*30)

masukkan = int(input('masukkan nilai : '))

if masukkan >= 90:
    print("nilai anda A")
elif masukkan >= 80:
    print("nilai anda B")
elif masukkan >= 70:
    print("nilai anda C")
elif masukkan >= 60:
    print("nilai anda D")
elif masukkan <= 60:
    print("nilai anda E")