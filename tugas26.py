print("="*30)
print("RUMUS FISIKA NEWTON I ")
print("="*30)

print('''KETERANGAN: 
MASA : satuan(kg)
GRAVITASI BUMI : satuan(m/s2)
GAYA : satuan(N)
RUMUS:
W = M.G
''')

print("DIKETAHUI")
masa = int(input("MASUKAN NILAI MASA?: "))
gravitasi_bumi = int(input("MASUKAN NILAI GRAVITASI BUMI? : "))

w = masa * gravitasi_bumi

print("JAWAB : ",w,'N')
