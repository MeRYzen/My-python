# Input
buyer = input("Input Nama Pembeli : ")
no = input("Input No. Handphone : ")
jurusan = input("Input Jurusan [SBY/BL/LMP : ")

# proses
if jurusan == "SBY":
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL":
    namajurusan = "Bali"
    harga = 350000
else:
    namajurusan = "Lampung"
    harga = 500000

# inputjmlhbeli
jumlah = int(input("Masukkan Jumlah Beli : "))

# proses potongan
if jumlah >= 3:
    potongan = (jumlah*harga) * 0.1
else:
    potongan = 0

total = (jumlah*harga) - potongan

# cetakahasil
print("-----------------------------------")
print("       PENJUALAN TIKET BUS")
print("              XYZ")
print("-----------------------------------")
print("Nama Pembeli : "+str(buyer))
print("No.Handphone : "+str(no))
print("Kode Jurusan yang dipilih : "+str(jurusan))
print("Harga        : ", +(harga))
print("Jumlah Beli  : ", +(jumlah))
print("-----------------------------------")
print("Potongan Yang Didapat : ", +(potongan))
print("Total Bayar           : ", +(total))
ubay = int(input("Masukkan Uang Bayar  : "))
uangkmbl = ubay-total
print("Uang Kembali    : ", +uangkmbl)
print("")
