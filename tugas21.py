print ("="*30)
print ("RUMUS MENGHITUNG KALOR FISIKA")
print ("="*30)

m = float(input("Masukan Nilai Masa : "))
c = float(input("Masukan Nilai Celsius : "))
dt = 0.5
l = float(input("Masukan Nilai Liter : "))

Q1 = m * c * dt
Q2 = m * l
Q3 = m * c * dt

if dt > 5 :
    print ("NORMAL")
elif dt < 0 :
    print ("TIDAK NORMAL")

print ("Hasil Kalor Lebur es :",Q1,)
print ("Hasil Kalor jenis air :",Q2,)
print ("Hasil Jumlah Kalor :",Q3,)