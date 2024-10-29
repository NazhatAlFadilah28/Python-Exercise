print("="*40)
print("RUMUS MENGHITUNG PERSEGI PANJANG")
print("="*40)

def persegi_panjang():
    l =int(input("MASUKAN NILAI LEBAR : "))
    p =int(input("MASUKAN NILAINLEBAR : "))
    t =int(input("MASUKAN NILAI TINGGI : "))
    luas = lambda : l * p
    volume = lambda : p * t * l
    keliling = lambda : 2 * p + l
    
    print("LUAS : ",luas(), 'cm2')
    print("VOLUME : ",volume(), 'cm2')
    print("KELILING : ",keliling(), 'cm2')

persegi_panjang()