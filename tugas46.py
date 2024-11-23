print("="*30)
print("MENGHITUNG NILAI UANG")
print("="*30)

uang = int(input("MASUKAN NILAI MATA UANG : RP."))

asal = uang

seribu = 1000
b = 500
c = 100
d = 50
e = 25

satu = int(uang / seribu)
uang %= seribu

dua = int(uang / b)
uang %= b

tiga = int(uang / c)
uang %= c

empat = int(uang / d)
uang %= d

lima = int(uang / e)
uang %= e

print(f'''
Uang senilai RP.{asal} setara dengan:
     {satu}\tpecahan RP. {seribu}
     {dua}\tpecahan RP. {b}
     {tiga}\tpecahan RP. {c}
     {empat}\tpecahan RP. {d}
     {lima}\tpecahan RP. {e}
''')