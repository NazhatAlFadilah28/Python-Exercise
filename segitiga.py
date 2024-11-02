print("="*30)
print("RUMUS KELILING SEGITIGA")
print("="*30)

def segitiga():
    sisi = int(input("MASUKAN NILAI SISI  : "))
    keliling = lambda s: sisi**3

    print("KELILING :",keliling(sisi),'cm2')

segitiga()
