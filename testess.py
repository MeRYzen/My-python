pil = "Y"
while pil == "Y":
    print("            TOKO PULSA")
    print(" ================================== ")
    kode = input("Masukan Kode provider[1/2/3] : ")
    if kode == "1":
        nmprov = "IM3"
    elif kode == "2":
        nmprov = "XL"
    elif kode == "3":
        nmprov = "Simpati"
    else:
        nmprov = ""
input("Nama Provider :" + str(nmprov))
jnspulsa = input("Masukan Jenis Pulsa : ")
if kode == "1":
    nmprov = "IM3"
    if jnspulsa == "im25":
        harga = 26000
    elif jnspulsa == "im50":
        harga = 52000
    elif jnspulsa == "im100":
        harga = 115000
    else:
        harga: 0
elif kode == "2":
    nmprov = "XL"
    if jnspulsa == "xl25":
        harga = 26500
    elif jnspulsa == "xl50":
        harga: 52500
    elif jnspulsa == "xl100":
        harga = 110000
    else:
        harga = 0
else:
    nmprov = "Simpati"
    if jnspulsa == "simp25":
        harga = 27000
    elif jnspulsa == "simp50":
        harga = 51500
    elif jnspulsa == "simp100":
        harga = 120000

print("Nama Provider :" + str(nmprov))
print("Jenis Provider :" + str(jnspulsa))
print("Harga : ", harga)
tobay = int(input("Masukan Total Bayar : "))
print("===================================")
kmbl = tobay-harga
print("Uang Kembali : ", kmbl)
pil = input("yaser =")
