total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    lembur = int(input("Masukkan jam lembur: "))

    while lembur < 0 or lembur == 5 or lembur == 7:
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    if lembur > 8:
        print("Jumlah lembur melebihi batas yang ditentukan!")
        upah_lembur = 0
    elif lembur == 0:
        upah_lembur = 0
    elif lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    else:
        upah_lembur = 300000

    malam = input("Shift malam? (y/n): ")

    if malam == "y":
        tambahan = 50000
    else:
        tambahan = 0

    gaji_harian = 100000 + upah_lembur + tambahan
    total_gaji += gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("\nTotal gaji mingguan: Rp", total_gaji)