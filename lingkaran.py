print("="*30)
print("RUMUS KELILING LINGKARAN")
print("="*30)

def lingkaran():
    phi = 3.14
    ruas = int(input('ruas\t\t: '))
    luas = lambda r: phi * ruas * ruas

    print('luas\t\t: ' ,luas(ruas), ' cm2')

lingkaran()
