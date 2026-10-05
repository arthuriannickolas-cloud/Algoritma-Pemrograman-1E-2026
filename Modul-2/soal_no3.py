suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("=== DATA REAKTOR ===")
print("Suhu Reaktor   :", suhu, "°C")
print("Tekanan Gas    :", tekanan, "Bar")

print("=== STATUS REAKTOR ===")

if suhu > 1000:
    if tekanan > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")

elif suhu > 500:
    if tekanan > 30:
        print("Tekanan Tidak Stabil")
    else:
        print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("=== STATUS POMPA AIR ===")
print(status_pompa)