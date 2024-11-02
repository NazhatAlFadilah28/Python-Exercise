print("="*30)
print("RUMUS JAJAR GENJANG")
print("="*30)

def jajar_genjang():
    alas = int(input("MASUKAN NILAI ALAS : "))
    tinggi = int(input("MASUKAN NILAI TINGGI : "))
    luas = lambda a,t: alas * tinggi

    print("HASIL : ",luas(alas,tinggi),'cm2')

jajar_genjang()
