# SOAL NO.3

jarak_satu_arah= float(input("Masukkan jarak satu arah: "))
tingkat_konsumsi_bensin_satu_liter = float(input("Masukkan tingkat konsumsi bensin sebanyak 1 liter: "))
harga_bensin_satu_liter = float(input("Masukkan harga bensin per liter: "))
sisa_bensin_sebelumnya = float(input("Masukkan banyaknya sisa bensin sebelumnya: "))

total_jarak_PP = (jarak_satu_arah)*2
total_kebutuhan_bensin = total_jarak_PP/tingkat_konsumsi_bensin_satu_liter
jumlah_bensin_yang_benar_benar_di_beli = total_kebutuhan_bensin-sisa_bensin_sebelumnya
total_biaya_yang_dikeluarkan_untuk_membeli_bensin = jumlah_bensin_yang_benar_benar_di_beli*harga_bensin_satu_liter

print("Total jarak PP: ", total_jarak_PP, "km")
print("Total kebutuhan bensin: ", total_kebutuhan_bensin, "liter")
print("Jumlah bensin yang benar-benar di beli: ", jumlah_bensin_yang_benar_benar_di_beli, "liter")
print("Total biaya yang dikeluarkan untuk membeli bensin: Rp.", total_biaya_yang_dikeluarkan_untuk_membeli_bensin,".-")