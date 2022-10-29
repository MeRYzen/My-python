# ini output judul
from traceback import print_tb


print("=================================")
print("      GEROBAK FRIED CHICKEN      ")
print("=================================")
print("Kode    Jenis Potong     Harga   ")
print("---------------------------------")
print(" D         Dada        Rp. 25.000 ")
print(" P         Paha        RP. 20.000 ")
print(" S         Sayap       Rp. 15.000 ")

list_kode = []
list_jenis = []
list_jml = []
list_jumhar = []
list_jenis = []
list_harga = []

jumbay = 0

data = int(input("Masukkan Banyak Jenis :"))

for i in range(data):
    print("Jenis Ke -", i+1)
    list_kode.append(input("Kode Potong [D/P/S] :"))
    list_jml.append(int(input("Banyak Beli :")))
    # proses seleksi
    if list_kode[i] == "D" or list_kode[i] == "d":
        list_jenis.append("Dada")
        list_harga.append(25000)
    elif list_kode[i] == "P" or list_kode[i] == "p":
        list_jenis.append("Paha")
        list_harga.append(20000)
    elif list_kode[i] == "S" or list_kode[i] == "s":
        list_jenis.append("Sayap")
        list_harga.append(15000)
    else:
        list_jenis.append("Salah input coeg")
        list_harga.append(0)

# proses hitung jumlah harga
for i in range(data):
    list_jumhar.append(list_harga[i]*list_jml[i])
    jumbay = jumbay+list_jumhar[i]

pajak = 0.10*jumbay
tobay = pajak + jumbay
print("GEROBAK FRIED CHICKEN")
print("------------------------------------------------")
print("no    Jenis    Harga     Banyak    Jumlah")
print("      Potong   Satuan    Beli      Harga")
print("------------------------------------------------")
# proses looping output
for i in range(data):
    print("%d     %s     %d      %d     %d" %
          (i+1, list_jenis[i], list_harga[i], list_jml[i], list_jumhar[i]))

print("------------------------------------------------")
print("  Jumlah Bayar : Rp. ", f"{jumbay:,}")
print("  Pajak  10%   : Rp. ", f"{pajak:,}")
print("  Total Bayar  : Rp. ", f"{tobay:,}")
ubay = int(input("      Uang Bayar   : Rp.  "))
ukem = ubay-tobay
print("     Uang Kembali : Rp. ", f"{ukem:,}")
