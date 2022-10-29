print("            TOKO PULSA")
print(" ================================== ")
print("             1.IM3")
print("             2.XL")
print("             3.Simpati")

kode = input("Masukan Kode provider[1/2/3] : ")
if kode == "1":
    nmprov = "IM3"
    nmprov = "IM3"
elif kode == "2":
    nmprov = "XL"
elif kode == "3":
    nmprov = "Simpati"
else:
    nmprov = ""
print("Nama Provider :" + str(nmprov))
if nmprov == "IM3":
    print("        IM3")
    print("      1.IM3 :25")
    print("      2.IM3 :50")
    print("      3.IM3 :100")
    print("==================================")
else:
    print("")


print("==================================")
if nmprov == "XL":
    print("        XL")
    print("      1.XL :25")
    print("      2.XL :50")
    print("      3.XL :100")
    print("==================================")
else:
    print("")


if nmprov == "Simpati":
    print("        SIMPATI")
    print("      1.SIMPATI :25")
    print("      2.SIMPATI :50")
    print("      3.SIMPATI :100")
    print("==================================")
else:
    print("")


jnspulsa = input("Masukan Jenis Pulsa : ")
if kode == "1":
    nmprov = "IM3"
    if jnspulsa == "1":
        harga = 26000
    elif jnspulsa == "2":
        harga = 52000
    elif jnspulsa == "3":
        harga = 115000
    else:
        harga: 0
elif kode == "2":
    nmprov = "XL"
    if jnspulsa == "1":
        harga = 26500
    elif jnspulsa == "2":
        harga: 52500
    elif jnspulsa == "3":
        harga = 110000
    else:
        harga = 0
else:
    nmprov = "Simpati"
    if jnspulsa == "1":
        harga = 27000
    elif jnspulsa == "2":
        harga = 51500
    elif jnspulsa == "3":
        harga = 120000

print("Nama Provider :" + str(nmprov))
print("Jenis Provider :" + str(jnspulsa))
print("Harga : ", harga)
tobay = int(input("Masukan Total Bayar : "))
print("==================================")
kmbl = tobay-harga
print("Uang Kembali : ", kmbl)
