print("Ketik 0 untuk berhenti.")

total_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = float(input("Masukkan jarak (km): "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid! Masukkan angka positif.")
        continue

    total_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if total_penumpang % 5 == 0:
        tarif = tarif / 2
        print(f"Penumpang ke-{total_penumpang} (DAPAT DISKON 50%!) - Bayar: Rp{int(tarif)}")
    else:
        print(f"Penumpang ke-{total_penumpang} - Bayar: Rp{tarif}")

    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print()

print("REKAPITULASI AKHIR")
if total_penumpang > 0:
    rata_jarak = total_jarak / total_penumpang
    print(f"Jumlah penumpang : {total_penumpang} orang")
    print(f"Total pendapatan : Rp{int(total_pendapatan)}")
    print(f"Jarak terjauh    : {jarak_terjauh} km")
    print(f"Rata-rata jarak  : {rata_jarak} km")
else:
    print("Tidak ada data penumpang.")
