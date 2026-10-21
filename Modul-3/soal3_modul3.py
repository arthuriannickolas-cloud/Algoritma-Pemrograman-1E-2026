jumlah_mahasiswa = 10

jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0

nilai_tertinggi = -1
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(jumlah_mahasiswa):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))

    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1
    total_nilai += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

    print("\nNama:", nama)
    print("Nilai Tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("Nilai Akhir:", nilai_akhir)
    print("Kategori:", kategori)

rata_rata = total_nilai / jumlah_mahasiswa

print("      REKAPITULASI NILAI KELAS ")
print("Jumlah mahasiswa kategori A:", jumlah_A)
print("Jumlah mahasiswa kategori B:", jumlah_B)
print("Jumlah mahasiswa kategori C:", jumlah_C)
print("Jumlah mahasiswa kategori D:", jumlah_D)
print("Jumlah mahasiswa kategori E:", jumlah_E)

print("Nilai akhir tertinggi:", nilai_tertinggi)
print("Nama mahasiswa:", nama_tertinggi)

print("Nilai akhir terendah:", nilai_terendah)
print("Nama mahasiswa:", nama_terendah)

print("Rata-rata nilai akhir:", rata_rata)
