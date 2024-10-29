nilai = int(input("masukan nilai : "))

if nilai > 90 or nilai >= 100 :
    print("A")
elif nilai > 80 or nilai >= 89 :
    print("B")
elif nilai > 70 or nilai >= 79 :
    print("C")
elif nilai > 60 or nilai <= 69 :
    print("D")
elif nilai < 60 :
    print("E")
else:
    print("NILAI SALAH")