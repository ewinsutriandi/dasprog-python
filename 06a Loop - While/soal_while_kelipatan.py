'''
Bilangan kelipatan 3 atau 5 di bawah 10 adalah 3,5,6,9
Jika dijumlahkan nilanya adalah 23
Buatlah sebuah program yang menghitung
jumlah bilangan kelipatan 3 atau 5 di bawah 1000

petunjuk: untuk memeriksa apakah suatu bilangan merupakan kelipatan bilangan yang lain, 
gunakan operator modulus 
jika n % m == 0 maka n adalah kelipatan m 
'''

bil = 1
total = 0
batas = 1000

while bil < batas:
    if bil % 3 == 0 or bil % 5 == 0:
        total = total + bil
    bil = bil +1

print(total)
