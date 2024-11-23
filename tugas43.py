print("="*30)
print("RUMUS ENERGI KINETIK")
print("="*30)

tegangan = float(input("MASUKAN JUMLAH TEGANGAN (volt)\t\t: "))
kuat_arus = float(input("MASUKAN JULAH KUAT ARUS (Ampere)\t\t: "))

hambatan = tegangan / kuat_arus

print(f"BESAR HAMBATAN YAITU : {hambatan} Ohm")    