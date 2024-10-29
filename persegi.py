print("="*30)
print("RUMUS MENGHITUNG LUAS PERSEGI")
print("="*30)

def persegi():
    sisi = int(input('sisi\t\t: '))
    luas = lambda s: s * s
    keliling = lambda s: 4 *s

    print('luas\t\t: ' ,luas(sisi), ' cm2')
    print('keliling\t: ',keliling(sisi), ' cm')

persegi()
persegi()
persegi()