print("="*30)
print("ANGKA ANGKA ROMAWI")
print("="*30)

angka = int(input('Masukkan angka 1-10 \t: '))
romawi = ['I', 'II', 'III','IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
if 1 <=  angka <= 10:
 print(f"{angka} DALAM ANGKA ROMAWI ADALAH : {romawi[angka-11]}")
else:
 print("SALAH")