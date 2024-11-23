print("="*30)
print("MENGHITUNG DERET ARITMATIKA")
print("="*30)

a = int(input('Masukkan suku pertama (a): '))
b = int(input('Masukkan suku beda (b): '))
n = int(input('Masukkan jumlah suku (n): '))

S_n = int(n / 2) * (2 * a + (n - 1) * b)

print('Jumlah deret aritmatika\t\t: ',S_n)