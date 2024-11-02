print("="*20)
print("PENGULANGAN 8")
print("="*20)

jumlah = 0
for a in range(1, 6):
    if a < 5:
        print(a,end=' + ')
    else:
        print(a,end=' = ')
    jumlah = jumlah + (a)
print(jumlah)