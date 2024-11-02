print("="*30)
print("RUMUS TABUNG")
print("="*30)
def tabung():
    phi = 3.14
    ruas = int(input("MASUKAN NILAI RUAS : "))
    tinggi = int(input("MASUKAN NILAI TINGGI : "))
    luas = lambda r,t: 2 * phi * r + t

    print("HASIL :",luas(ruas,tinggi),'cm2')

tabung()
