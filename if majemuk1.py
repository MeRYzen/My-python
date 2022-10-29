print("     Warteg sans sini bersih")
print("=================================")
print("     MENU Makanan Restoran")
print("=================================")
print("Paket Kenyang 1")
print("1. Paket Kenyang 1")
print(" Menu : Nasi Putih + Ayam Goreng + Es teh Manis ")
print(" Harga =100000")
print("1. Paket kenyang 2")
print(" Menu : Nasi Putih + Ayam Goreng + Es teh Manis")
print(" Harga =75000")
print("1. Paket Kenyang 3")
print(" Menu : Kentang Goreng + Humberger")
print(" Harga =50000")
print("=================================")

# paket

paket = input("Pilih Paket Makanan [1/2/3] : ")
if paket == "1":
    menu = "Nasi Uduk + Kentang Goreng + Ayam Goreng + Es Teh Manis"
    harga = 100000
elif paket == "2":
    menu = "nasi putih + Ayam Goreng"
    harga = 75000
elif paket == "3":
    menu = "Kentang Goreng + Humberger"
    harga = 50000
else:
    menu = ""
    harga = 0
jml_beli = int(input("Masukan Jumlah Beli : "))
total_bayar = harga*jml_beli
print("     Warteg sana sini Bersih")
print("=================================")
print("Pilihan Paket : " + str(paket))
print("Menu Makanan : " + str(menu))
print("Harga Makanan : ", harga)
print("Jumlah Beli : ", jml_beli)
print("======================================")
print("Total Bayar        : ", total_bayar)
uang_bayar = int(input("Masukan Uang Bayar : "))
ukem = uang_bayar-total_bayar
print("======================================")
print("Uang Kembali = ", ukem)
