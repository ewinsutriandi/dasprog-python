'''
Buatlah program yang menerima input sebuah bilangan bulat n
kemudian mencetak piramida dengan n baris 
seperti pada ilustrasi berikut
        *              1
      * * *            3
    * * * * *          5
  * * * * * * *        7
* * * * * * * * *      9
dst
'''
n = int(input("Masukkan sebuah bilangan bulat: "))

for i in range(n): # perulangan sejumlah baris yang diinginkan
    for k in range(n-i-1):
        print("  ",end="")
    for j in range(i+1+i): # perulangan sejumlah bintang yg dicetak
        print("* ", end="") # agar tidak ganti baris
    print() # ganti baris sesuai i