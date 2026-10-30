n = int(input("masukkan bilangan bulat positif: "))
for i in range(1, n + 1):
    j = n - i + 1

    for spasi in range(n - i):
        print("  ", end="")
    for angka_naik in range(1, i + 1):
        print(angka_naik, end=" ")
    for angka_turun in range(i - 1, 0, -1):
        print(angka_turun, end=" ")
    for spasi in range(n - i): 
        print("  ", end="")
 
    print("   ", end="")  

    for spasi in range(n - j):
        print("  ", end="")
    for angka_naik in range(1, j + 1):
        print(angka_naik, end=" ")
    for angka_turun in range(j - 1, 0, -1):
        print(angka_turun, end=" ")

    print()