x = int(input("masukkan nilai dari x :"))
y = int(input("masukkan nilai dari y :"))
z = int(input("masukkan nilai dari z :"))

if x > y and y > z:
 print ("nilai terbesar :",x)
 print ("nilai terkecil :",z)
elif x > y and y < z:
 print ("nilai terbesar :",y)
 print ("nilai terkecil :",z)
elif y > x and x < z:
 print ("nilai terbesar :",y)
 print ("nilai terkecil :",x)
elif z > y and y < x:
 print ("nilai terbesar :",z)
 print ("nilai terkecil :",y)
elif x < y and y < z:
 print ("nilai terbesar :",z)
 print ("nilai terkecil :",x)