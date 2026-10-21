while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))
    if 2 <= n <= 15: #memeriksa apakah nilai n berada di antara 2 sampai 15.
        break
    print("Input tidak valid! Masukkan angka 2 sampai 15.")

for i in range(1, 2 * n): #mengatur jumlah baris yang akan dicetak.
    baris = i if i <= n else 2 * n - i #menghasilkan angka mulai dari 1 sampai sebelum 2 * n.
#Jika i kurang dari atau sama dengan n, nilai baris adalah i. Jika tidak, nilai baris adalah 2 * n - i
    hasil = " " * (n - baris)

    for j in range(1, baris + 1):
        hasil += str(j % 10)

    for j in range(baris - 1, 0, -1):
        hasil += str(j % 10)

    print(hasil)
    