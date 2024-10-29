total_harga = float(input("masukan total harga barang :"))

discount = (5)

if total_harga >= 100000:
    discount = 0,5 * total_harga

total_setelah_discount = total_harga -discount

print("total discount yang di dapat",discount)
print("total yang harus di bayar :",total_setelah_discount)

