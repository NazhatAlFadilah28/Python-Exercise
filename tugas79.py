print("="*30)
print("DISKON GACOAN")
print("="*30)

menu={
    "pizza":20000,
    "mie gacoan":10000,
    "Kebab":10000,
}
print(menu)

m=int(input('masukan total belanja:\t'))

if m > 50000:
    total = m - 5000
    print(total)
    