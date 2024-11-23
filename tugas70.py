print("="*30)
print("RUMUS MENGHITUNG SUKU")
print("="*30)

a = int(input('Masukkan suku pertama (a): '))
b = int(input('Masukkan beda (b): '))
n = int(input('Masukkan nomor suku (n): '))

Un = a + (n - 1) * b

print(f'Suku ke-{n}\t\t: {Un}')