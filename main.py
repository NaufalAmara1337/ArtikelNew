import string
import mylib



def main():
    while True:
        inputUserMenu = input('''
Selamat datang di CryptingBeGone, aplikasi pesan pendek agar orang lain tidak mengetahui isi kepala anda!
    1. Caesar
    2. Vigenere
    3. Custom
    4. Keluar
silahkan pilih cipher yang anda inginkan: ''')

        print(inputUserMenu)

        if inputUserMenu == '1':
            mylib.caesar_main()
        elif inputUserMenu == '2':
            mylib.vigenere()
        elif inputUserMenu == '3':
            mylib.customCipher()
        elif inputUserMenu == '4':
            print('Terima kasih untuk penggunaan program ini!')
            break
        else:
            print('Pilihan tidak ada')
    

main()