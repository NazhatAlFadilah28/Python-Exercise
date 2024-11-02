print("="*30)
print("RUMUS VOLUME KUBUS")
print("="*30)

def kubus():
    sisi = int(input("MASUKAN NILAI SISI : "))
    volume = lambda s: sisi**3

    print("VOLUME : ",volume(sisi),'cm2')

kubus()