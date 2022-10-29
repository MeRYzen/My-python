print("============biaya beli telor============")

brt = int(input("Masukan berat="))
hrg = int(input("Masukan harga="))
ongkos = int(input("Masukan ongkos="))
uang = int(input("Masukan uang ibu="))
sisauang = uang-ongkos*2-hrg*brt
print("Sisa uang ibu adalah  %s" % (sisauang))
