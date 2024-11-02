print("="*30)
print("RUMUS KELILING TRAPESIUM")
print("="*30)

def trapesium():
    sisi = int(input("MASUKAN NILAI SISI : "))
    panjang = lambda s: sisi**4

    print("PANJANG :",panjang(sisi),'cm')

trapesium()
