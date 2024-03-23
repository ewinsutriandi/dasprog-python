'''
Buatlah program yang menerima input sebuah bilangan bulat n
kemudian mencetak segitiga siku-siku dengan n baris 
seperti pola pada ilustrasi berikut
             i  spasi
        *    0     8       
      * *    1     6
    * * *    2     4
  * * * *    3     2
* * * * *    4     0
dst
'''

n = int(input("Masukkan sebuah bilangan bulat: "))

for i in range(n): # perulangan sejumlah baris yang diinginkan
    for k in range(n-i-1): # perulangan untuk mencetak indent (spasi sebelah kiri bintang)
        print("  ",end="")
    for j in range(i+1): # perulangan sejumlah bintang yg dicetak
        print("* ", end="") # agar tidak ganti baris
    print() # ganti baris sesuai i