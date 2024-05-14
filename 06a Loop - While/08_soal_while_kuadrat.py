'''
Jumlah bilangan kuadrat yang lebih kecil atau sama dengan 10 adalah: 1 + 4 + 9 = 14
Hitung jumlah bilangan kuadrat yang lebih kecil atau sama dengan 10000
'''
b = 1
total = 0
batas = 20
while b**2 <= batas:
    total = total + b ** 2
    b = b + 1
print(total)
