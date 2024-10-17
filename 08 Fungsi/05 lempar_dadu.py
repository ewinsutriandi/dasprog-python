import random
def lempar_dadu():
    ''' Fungsi lempar dadu
    Menghasilkan bilangan acak dari 1 s.d 6
    Seperti dadu yang di lempar
    '''
    return random.randint(1,6)


# contoh cara pemakaian, melempar dadu sebanyak 5 kali dan mencetak nilai yg muncul
for i in range(5):
    print(lempar_dadu())