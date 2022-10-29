print("          YOVIE COFFE        ")
print("=====================================")

nama = input(" Nama Pelanggan : ")
tanggal = input("Tanggal Pembelian : ")
print("=====================================")
print("     ======MENU======")
print("1. Iced Tea                  Rp.6000")
print("2. Caramel Machiato          Rp.30000")
print("3. Grend Tea Latte           Rp.25000")
print("4. Milkshake                 Rp.15000")
print("     ======MENU======")
h = []
a = 1
menu_pesanan = int(input("Masukan Menu Pesanan (Nomor Menu) :  "))
if menu_pesanan == 1:
    harga = 6000
elif menu_pesanan == 2:
    harga = 30000
elif menu_pesanan == 3:
    harga = 25000
elif menu_pesanan == 4:
    harga = 15000
else:
    while True:
        print("===== Menu Tidak Tersedia silahkan Pilih Menu lainya :) ====")
        menu_pesanan = int(input("Masukan Menu Pesanan (Nomor Menu): "))
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4:
            if menu_pesanan == 1:
                harga = 6000
            elif menu_pesanan == 2:
                harga = 30000
            elif menu_pesanan == 3:
                harga = 25000
            elif menu_pesanan == 4:
                harga = 15000
                break
jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))
for i in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input(
        "Apakah ada yang ingin ditambahkan/dikurangi? tambah/kurang/tidak ")
    if jawab == 'tambah':
        tambah = int(input("Masukan Menu Pesanan (Nomor Menu): "))
        if tambah == 1:
            harga = 6000
        elif tambah == 2:
            harga = 30000
        elif tambah == 3:
            harga = 25000
        elif tambah == 4:
            harga = 15000
        jumlah_tambahan = int(input("Masukan Jumlah Pembelian : "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c = jumlah_tambahan+jumlah_pembelian
        print("Total Pesanan :  ", c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    elif jawab == 'kurang':
        kurang = int(input("Berapa Jumlah yang dikurangkan ? "))
        for i in range(kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h[kurang]
                if kurang < 0:
                    break
        c = jumlah_pembelian - kurang
        print("Total Pemesanan ", c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    else:
        bayar = sum(h)
        c = jumlah_pembelian
        print("Total Pemesanan", c)
        print("Total Pembayaran : Rp. ".format(bayar))
    break
