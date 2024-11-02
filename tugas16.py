print("="*40)
print("\tLIST HEWAN HEWAN SAFARI\t")
print("="*40)

nama = ['Zebra','Jerapah','Singa','Kuda','Kuda Nil','Impala','Macan Tutul']
nama[2] = 'Raja Hutan'
nama.append('Gajah')

for i,x,in enumerate(nama):
    print(i+1,'.',x)