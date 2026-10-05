pin = int(input("Masukkan 3 digit PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

digit_pertama = pin // 100
digit_kedua = (pin // 10) % 10
digit_ketiga = pin % 10

print("Digit Pertama : ", digit_pertama)
print("Digit Kedua   : ", digit_kedua)
print("Digit Ketiga  : ", digit_ketiga)

if pin % 5 == 0:
    if jam < 12:
        status_pintu = "Garasi Pagi Terbuka"
    else:
        status_pintu = "Garasi Malam Terbuka, Lampu Dinyalakan" 
elif pin % 2 == 0:
    if (digit_pertama + digit_ketiga) == digit_kedua:
        status_pintu = "Garasi VIP Terbuka Khusus Bos"
    else:
        status_pintu = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status_pintu = "Akses Ditolak Sepenuhnya"

print("Status Pintu  : ", status_pintu)

status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
print("Status CCTV   : ", status_cctv)