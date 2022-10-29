print("Halo Selamat Datang Di Coffe Shop")

name = input("Siapa nama mu?\n")
print("Hi " + name + " Selamat Datang Di Coffe Shop\n\n")

print("===========  LIST MENU  ===========")
print("    1. Black Coffee ==> Rp25.000")
print("    2. Espresso     ==> Rp30.000")
print("    3. Latte        ==> Rp37.000")
print("    4. Cappucino    ==> Rp35.000")
print("    5. Macchiato    ==> Rp40.000")


print("===================================\n\n")

listmenu = input("Pilih Menu: ")
print("")
pesanan = input("Jumlah Di Pesan: ")

if listmenu == "1":
    menu = "Black Coffee"
    harga = 25000
    total = 25000 * int(pesanan)
elif listmenu == "2":
    menu = "Espresso"
    harga = 30000
    total = 30000 * int(pesanan)
elif listmenu == "3":
    menu = "Latte"
    harga = 37000
    total = 37000 * int(pesanan)
elif listmenu == "4":
    menu = "Cappucino"
    harga = 35000
    total = 35000 * int(pesanan)
elif listmenu == "5":
    menu = "Macchiato"
    harga = 40000
    total = 40000 * int(pesanan)


print("==============================")
print("Nama Pembeli   = " + name)
print("")
print("Menu           = " + menu)
print("")
print("Harga          = Rp" + str(harga))
print("")
print("Jumlah Di beli = " + pesanan)
print("")
print("Total          = Rp" + str(total))
print("==========Thank You===========")
