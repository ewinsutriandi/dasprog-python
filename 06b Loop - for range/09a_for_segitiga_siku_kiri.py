'''
Buatlah program yang menerima input sebuah bilangan bulat n
kemudian mencetak segitiga siku-siku dengan n baris 
seperti pada ilustrasi berikut
*             1  0
* *           2  1
* * *         3  2
* * * *       4  3
* * * * *     5  4
dst
'''

n = int(input("Masukkan sebuah bilangan bulat:"))

for i in range(n): # perulangan sejumlah baris yang diinginkan
    for j in range(i+1): # perulangan sejumlah bintang yg dicetak
        print("* ", end="") # agar tidak ganti baris
    print() # ganti baris sesuai i