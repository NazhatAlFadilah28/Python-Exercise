print("="*30)
print("RUMUS PRISMA SEGITIGA")
print("="*30)

def prisma_segitiga():
    alas = int(input("MASUKAN NILAI ALAS : "))
    tinggi = int(input("MASUKAN NILAI TINGGI : "))
    volume = lambda a,t: alas *tinggi

    print("VOLUME : ",volume(alas,tinggi),'cm2')

prisma_segitiga()