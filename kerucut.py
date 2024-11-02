print("="*30)
print("RUMUS GEOMETRI KERUCUT")
print("="*30)

def kerucut():
    phi = 3.14
    ruas = int(input("MASUKAN NILAI RUAS : "))
    tinggi = int(input("MASUKAN NILAI TINGGI : "))
    suku = int(input("MASUKAN NILAI SUKU : "))
    luas_permukaan = lambda r,s: (phi * ruas * suku) + (phi * ruas**2)
    volume = lambda r,t: 1/2 * phi * ruas * ruas * tinggi

    print("LUAS PERMUKAAN : ",luas_permukaan(ruas,suku),'cm3')
    print("VOLUME : ",volume(ruas,tinggi),'cm2')

kerucut()

    
