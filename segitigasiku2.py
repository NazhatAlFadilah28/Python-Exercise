print("="*40)
print("RUMUS MENGHITUNG SEGITIGA SIKU SIKU")
print("="*40)

def segitiga_siku_siku():
    a =int(input("MASUKAN NILAI ALAS : "))
    t =int(input("MASUKAN NILAI TINGGI : "))
    s =int(input("MASUKAN NILAU SISI : "))
    luas = lambda : 1/2 * a *t 
    keliling = lambda : s * s * s

    print("LUAS : ",luas (), 'cm2')
    print("keliling : ",luas (), 'cm2')

segitiga_siku_siku()