'''
Buatlah program yang mencari kemudian mencetak nilai maksimum dari list berikut
'''

nilai_uts_mhs = [56,76,85,90,95,67,88,32,25]
nil_maks = 0
for nil in nilai_uts_mhs:
    if nil > nil_maks:
        nil_maks = nil
print("Nilai terbesar", nil_maks)

