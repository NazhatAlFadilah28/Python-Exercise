print("="*40)
print("\t\tRUMUS BOLA\t\t")
print("="*40)

def lingkaran():
    phi = 3.14
    ruas = int(input("MASUKAN NILAI RUAS : "))
    volume = lambda r: 4/3 * phi * r**3
    luas_permukaan = lambda r: 4 * phi * r**2

    print("VOLUME : ",volume(ruas),'cm2')
    print("LUAS PERMUKAAN : ",luas_permukaan(ruas),'n2')

lingkaran()
