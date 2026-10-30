JumlahBarisLampu = int(input("masukkan jumlah baris lampu: "))
JumlahLampu = int(input("masukkan jumlah lampu: "))

for NomorBaris in range(1, JumlahBarisLampu + 1):
    print("baris", NomorBaris)
    for NomorLampu in range(1, JumlahLampu + 1):
        if NomorLampu % 3 == 0:
            print("Lampu", NomorLampu, "Mengalami gangguan")
        elif NomorLampu % 2 == 0:
            print("Lampu", NomorLampu, "Mengalami rusak")
        else:
            print("Lampu", NomorLampu, "berfungsi dengan baik")
print("PERIKSA SUMBER LISTRIK UTAMA TAMAN !")