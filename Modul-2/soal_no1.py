kode = int(input("Masukkan 3 digit kode: "))

d1 = kode // 100
d2 = (kode % 100) // 10
d3 = kode % 10

pelacak_awal = d1 * d3
tahap1 = (pelacak_awal + 25) if (d2 % 2 != 0) else (pelacak_awal - d2)
nilai_akhir = (tahap1 // 3) if (tahap1 % 3 == 0) else (tahap1 * 2)

if nilai_akhir > 50:
    status = "Kategori A"
elif nilai_akhir > 20:
    status = "Kategori B"
else:
    status = "Password Ditolak"

siklus = "Siklus Genap" if (nilai_akhir % 2 == 0) else "Siklus Ganjil"

# Output Hasil
print("Digit        : " , d1, d2, d3)
print("Pelacak Awal : " , pelacak_awal)
print("Tahap 1      : " , tahap1)
print("Nilai Akhir  : " , nilai_akhir)
print("Status       : " , status)
print("Siklus       : " , siklus)