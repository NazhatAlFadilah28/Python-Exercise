print("="*40)
print("INFORMASI JUKNIS PERLOMBAAN")
print("="*40)

print("="*30)
print("1. JUKNIS LOMBA SEPAKBOLA")
print("2. JUKNIS LOMBA VOLI")
print("3. JUKNIS LOMBA PUISI")
print("4. JUKNIS LOMBA GAME ONLINE")
print("="*30)

informasi = int(input("MASUKAN NOMOR INFORMASI LOMBA APA? : "))

if informasi == 1:
    print('''
    LOMBA SEPAK BOLA DIMULAI HARI SENIN TANGGAL 27-9-2024
    PERJURUSAN 2 PESERTA PERKELAS
    KETENTUAN:
    1. PESERTA WAJIB ANAK SEKOLAH SMK NEGERI 1 CIANJUR
    2. BOLEH MEMAKAI BAJU BOLA
    3. TIDAK BOLEH MEMAKAI BAJU LENGAN PENDEK
    4. TIDAK BOLEH RUSUH SAAT MAIN BOLA
    5. HARUS ADA SUPPORTER PERKELASNYA
    6. WAJIB MEMAKAI SEPATU
    7. WAJIB MEMAKAI KAOSKAKI PANJANG
    8. HARUS MENJAGA AHKLAK
    9. TIDAK BOLEH RIBUT
    10. HARUS MENGIKUTI ARAHAN PANITIA LOMBA
    ''')
elif informasi == 2:
    print(''' LOMBA VOLI DIMULAI HARI SELASA TANGGAL 27-9-2024
    PERJURUSAN 6 PESERTA PERKELAS
    KETENTUAN:
    1. PESERTA WAJIB HADIR
    2. BOLEH MEMAKAI BAJU OLAH RAGA ATAU GRUP
    3. TIDAK BOLEH MEMAKAI SEPATU
    4. TIDAK BOLEH BERISIK
    5. HARUS ADA SUPPORTER PERKELAS
    6. WAJIB MEMAKAI SEPATU
    7. WAJIB MEMAKAI KAOS KAKI PANJANG
    8. PESERTA WAJIB MENYAPA PANITIA
    9. TIDAK BOLEH BERKATA KASAR
    10. HARUS MENGIKUTI ARAHAN PANITIA LOMBA
    ''')
elif informasi == 3:
    print(''' LOMBA PIDATO DIMULAI HARI RABU TANGGAL 28-9-2024
    PERJURUSAN 1 PESERTA PERKELAS
    KETENTUAN:
    1. PESERTA WAJIB ANAK SEKOLAH SMK NEGERI 1 CIANJUR
    2. BOLEH MEMAKAI BAJU FORMAL
    3. PESERTA WAJIB MEMBUAT PUISI DI KERTAS A4
    4. PESERTA TIDAK BOLEH COPY PUISI ORANG
    5. PESERTA MEMAKAI SEPATU BEBAS
    6. PESERTA TIDAK BOLEH MEMAKAI PAKAIAN BEBAS
    7. WAJIB MEMAKAI KAOSKAKI PANJANG
    8. HARUS MENJAGA ATITTUDE
    9. HARUS RAPIH DALAM BERPAKAIAN
    10. HARUS MENGIKUTI ARAHAN PANITIA LOMBA''')
elif informasi == 4:
    print(''' LOMBA PIDATO DIMULAI HARI RABU TANGGAL 25-9-2024
    PERJURUSAN 5 PESERTA PERKELAS
    KETENTUAN:
    1. PESERTA WAJIB ANAK SEKOLAH SMK NEGERI 1 CIANJUR
    2. BOLEH MEMAKAI BAJU FORMAL
    3. PESERTA WAJIB MEMBAWA HP
    4. PESERTA WAJIB PUNYA KUOTA
    5. PESERTA MEMAKAI SEPATU BEBAS
    6. PESERTA TIDAK BOLEH MEMAKAI PAKAIAN BEBAS
    7. WAJIB MEMAKAI KAOSKAKI PANJANG
    8. HARUS MENJAGA ATITTUDE
    9. HARUS RAPIH DALAM BERPAKAIAN
    10. HARUS MENGIKUTI ARAHAN PANITIA LOMBA''')