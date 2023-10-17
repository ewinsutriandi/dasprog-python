'''
Dalam ilmu matematika, faktorial dari bilangan bulat positif dari n 
yang dilambangkan dengan n!, 
adalah hasil perkalian seluruh bilangan positif mulai dari n s.d 1.
0! = 1
1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 = 6
4! = 4 * 6 = 24
5! = 5 * 24 = 120
6! = 6 * 120 = 720
.
.
n! = n * (n-1)!

Buat sebuah fungsi rekursif yang menghitung nilai faktorial 
sebuah bilangan positif n

'''

def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n-1)
    
for i in range(7):
    print(faktorial(i), end=" ")

    