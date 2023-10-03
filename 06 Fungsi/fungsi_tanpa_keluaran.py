'''
Contoh fungsi tanpa masukan, dan tanpa keluaran
'''
def say_hello():
    print("Hello")

'''
Contoh fungsi dengan masukan, tanpa keluaran
'''
def say_hello_to(nama):
    print("Hello",nama)

'''
Contoh fungsi dengan beberapa masukan (parameter), tanpa keluaran
'''
def say_selamat(nama,event):
    print(f"Selamat {event}, {nama}")


say_hello_to("Upin")
say_selamat("Upin","ulang tahun")
say_selamat("Jarjit","wisuda")


