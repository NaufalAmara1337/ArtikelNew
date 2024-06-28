import string
import random


def caesar_encrypt(text, shift):
    text = text.lower()
    encryptedText = ''
    for char in text:
        if char.isalpha():  
            encryptedText += chr((ord(char)+shift - 97) % 26 + 97)
        else:
            encryptedText += char  
    return encryptedText

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_main():
    message = input('silahkan masukan teks: ')
    geser = int(input('silahkan masukan pergeseran kata: '))
    encryptedMessage = caesar_encrypt(message, geser)
    decryptedMessage = caesar_decrypt(encryptedMessage,geser)
    print(f'Kata yang di enkripsi: {encryptedMessage}')
    print(f'Kata yang di enkripsi: {decryptedMessage}')

def vigenere():
    while True:    
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        # Getting input from the user
        text = input('Please enter the text: ')
        custom_key = input('Please enter the key: ')
        direction = 1
        # direction = input('Enter 1 for encryption or -1 for decryption: ')
        # if direction == '1':
        #     direction = 1
        # if direction == '-1':
        #     direction = -1
        
        key_index = 0
        final_message = ''
        
        for char in text:
            if char.isalpha():
                # Determine if the character is uppercase or lowercase
                is_upper = char.isupper()
                char = char.lower()
                
                key_char = custom_key[key_index % len(custom_key)].lower()
                key_index += 1

                offset = alphabet.index(key_char)
                index = alphabet.index(char)
                new_index = (index + offset * direction) % len(alphabet)
                new_char = alphabet[new_index]

                # Convert back to uppercase if the original character was uppercase
                if is_upper:
                    new_char = new_char.upper()
                
                final_message += new_char
            else:
                final_message += char
        
        print(f'Teks yang di masukan: {text}')
        print(f'Teks yang di enkripsi: {final_message}')

        # Ask user if they want to encrypt/decrypt another message
        continue_choice = input('Do you want to encrypt/decrypt another message? (yes/no): ').strip().lower()
        if continue_choice != 'yes':
            break

    return final_message


def customCipher():

    char = ' ' + string.punctuation + string.ascii_letters + string.digits
    char = list(char)
    key = char.copy()

    random.shuffle(key)

    print('''Anda telah memilih cipher substitusi!:
''')
    plainText = input('Silahkan masukan teks: ')
    cipherText = ''

    for letter in plainText:
        id = char.index(letter)
        cipherText += key[id]

    #dekripsi
    encryptedText = cipherText
    decryptedText = ''

    for letter in plainText:
        id = key.index(letter)
        decryptedText += key[id]

    print(f'Teks enkripsi: {cipherText}')
    print(f'Teks dekripsi: {decryptedText}')


