kuota_penuh = 0

for i in range(1, 11):
    print ("===Data Mahasiswa ke-", i, "===")
    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK mahasiswa: "))

    if ipk <= 3.5:
        print ("Tidak memenuhi syarat untuk mendapatkan kuota beasiswa.")
        continue
    penghasilan = float(input("Masukkan penghasilan orang tua mahasiswa: "))
    
    if penghasilan >= 5000000:
        print ("Tidak memenuhi syarat untuk mendapatkan kuota beasiswa.")
        continue
    if penghasilan <= 3000000:
        kuota_penuh += 1
        print ("Selamat! Anda Mendapatkan kuota beasiswa penuh.")
    if penghasilan in range(3000000, 5000001):
        print ("Selamat! Anda Mendapatkan kuota beasiswa Sebagian.")
    if kuota_penuh == 3:
        print ("Kuota beasiswa penuh. Tidak ada lagi kuota beasiswa yang tersedia.")
        break
