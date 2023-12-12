from models import Menu,Pesanan,Tamu
import time

# Menu
ayam_goreng = Menu("Ayam goreng","makanan utama",12000)
nila_bakar = Menu("Nila bakar","makanan utama",12500)
tahu_isi = Menu("Tahu isi","Snack",5000)
es_teh = Menu("Es teh manis","Minuman",4500)
nasi_bakul = Menu("Nasi 1 bakul", "makanan utama",25000)
nasi_piring = Menu("Sepiring nasi","makanan utama",3500)

# tamu
tamu1 = Tamu("Meja 1")

tamu1.pesan(ayam_goreng,3)
tamu1.pesan(nila_bakar,2)
tamu1.pesan(nasi_bakul,1)
tamu1.pesan(tahu_isi,2)
tamu1.pesan(es_teh,5)
time.sleep(3)
tamu1.bayar("Tunai")


print(tamu1)