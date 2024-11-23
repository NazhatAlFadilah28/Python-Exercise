print("="*30)
print("USIA")
print("="*30)

def is_adult(age):
    return umur >= 18

umur = int(input("Masukkan usia: "))
if is_adult(umur):
    print("usia kamu di atas 18 tahun.")
else:
    print("usia kamu di bawah 18 tahun.")