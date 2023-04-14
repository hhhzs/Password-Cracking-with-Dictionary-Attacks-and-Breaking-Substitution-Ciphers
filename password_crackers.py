import hashlib

# https://www.mobilefish.com/services/hash_generator/hash_generator.php
# MD5 32digit
# SHA1 40digit
# SHA224 56digit
# SHA256 64digit
# SHA384 96digit
# SHA512 128digit
# user1:2224e8c5299874a5fe44a8de2f31c94e  32 -> MD5
# user2:e90829e04a20e9b49a4178f65b9a1a725191bd99fbd8071fa9cb6ee2552f2bc5 64 -> SHA256
# user3:6de664f06c446616eb374e1ba109a24b9172929162937831b18d7812fc76e1a3a8c9f4d1443d300b1b6a0419e80572ab0d5788f5faf28c869e06c84fe0242d96  128 -> SHA512
# user4:21d5c27a7e06317d1d02e0135a76454971e2c6d2  40 -> SHA1
# user5:aec0e78824de1205cf98384780983c6f2b7c03f8a6e5036a508ece76f1b3c5a7 64 -> SHA256
# user6:fa5da9b79da364f5aea54b2b9cdedaa4fff6f522be7f1e2b5f13f399bd1c94ca059220d7fd1fed2a31a60068c2d13007da7bf987b1623a7fc0ada0390fafb584  128 -> SHA512
# user7:dfa1339508e1b702a4588a3209a8e0ec  32 -> MD5
# CONCLUSION: user1 md5
# \user2 sha256 (with SALT)
# \user3 sha512 with caesar cipher
# \user4 sha1 (with leet speak)
# \user5 sha256
# \user6 sha512
# \user7 md5 with substitution ciphers
# \SALT and leet speak unknown (which means it will help a lot if we know which one used SALT or leet speak)
# I am assuming that in this assignment user won't use SALT and leet speak(or any other combo) at the same time
# In other words, SALT, leet speak, caesar cipher and substitution cipher are independent
import string


def md5_cracker_test(Input):  # use this to test if user1 has any SALT or leet speak
    with open('dictionary.txt') as dic:
        password = dic.readline().strip('\n')
        while password:
            PasswordInHex = hashlib.md5(password.encode('utf-8'))
            if PasswordInHex.hexdigest() == Input:
                print(password)
                exit()
            password = dic.readline().strip('\n')
        dic.close()
        # this gives user1 password: matrix123 with no any other cipher


'''
def sha1_cracker_test(Input):  # use this function to test if user4 has any cipher
    with open('dictionary.txt') as dic:
        word = dic.readline().strip('\n')
        while word:
            hashedWord = hashlib.sha1(word.encode('utf-8'))
            if hashedWord.hexdigest() == Input:
                print(word)
                exit()
            word = dic.readline().strip('\n')
        dic.close()
        # this gives nothing which means user4 has either SALT or leet speak
'''


def sha1_cracker_leet_speak_test(Input):
    with open('dictionary.txt') as dic:
        password = dic.readline().strip('\n')
        while password:
            password0 = password
            password1 = password0.replace('o', '0')  # this part is pain in the ass since it didnt say which
            password2 = password1.replace('l', '1')  # leet translate is used
            # password = password.replace('r', '2')
            password3 = password2.replace('e', '3')
            password4 = password3.replace('a', '4')
            password5 = password4.replace('s', '5')
            password6 = password5.replace('G', '6')
            password7 = password6.replace('T', '7')
            password8 = password7.replace('B', '8')
            password9 = password8.replace('g', '9')
            PasswordInHex = hashlib.sha1(password9.encode('utf-8'))
            if PasswordInHex.hexdigest() == Input:
                print(password)
                exit()
            password = dic.readline().strip('\n')
        dic.close()
        # this gives user4 password: r0u5534u with sha1 and leet speak, which by elimination user2 is using SALT


def sha256_cracker(Input):  # by elimination user5 is easy sha256 without any other cipher, Lets test it!
    with open('dictionary.txt') as dic:
        password = dic.readline().strip('\n')
        while password:
            PasswordInHex = hashlib.sha256(password.encode('utf-8'))
            if PasswordInHex.hexdigest() == Input:
                print(password)
                exit()
            password = dic.readline().strip('\n')
        dic.close()
        # this gives user5 password: josephine with sha256 and no cipher, which means my elimination is correct!


def sha512_cracker(Input):  # by elimination user6 is sha512 without any other cipher
    with open('dictionary.txt') as dic:
        password = dic.readline().strip('\n')
        while password:
            PasswordInHex = hashlib.sha512(password.encode('utf-8'))
            if PasswordInHex.hexdigest() == Input:
                print(password)
                exit()
            password = dic.readline().strip('\n')
        dic.close()
        # this gives user6 password: pumpkin1 with sha512 and no cipher


def getTranslatedMessage(Input, key):
    translated = ''
    for symbol in Input:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


def sha512_with_caesar_cipher(Input):  # this will solve user3
    with open('dictionary.txt') as dic:
        password = dic.readline().strip('\n')
        while password:
            for i in range(1, 27):
                s = getTranslatedMessage(password, i)
                PasswordInHex = hashlib.sha512(s.encode('utf-8'))
                if PasswordInHex.hexdigest() == Input:
                    print(password)
                    exit()
            password = dic.readline().strip('\n')
        dic.close()


def sha256_with_SALT(Input):
    with open('dictionary.txt') as dic:
        password = dic.readline().strip('\n')
        while password:
            for num in range(99999):
                SALT = str(num).zfill(5)
                # print(SALT)
                newpassword = password + SALT
                # print(newpassword)
                PasswordInHex = hashlib.sha256(newpassword.encode('utf-8'))
                if PasswordInHex.hexdigest() == Input:
                    print(password)
                    exit()
            password = dic.readline().strip('\n')
        dic.close()


def substitution_cipher_decoder(Input):
    Key = "sgquntivdaejrozhpyfclwxmkb"  # from part two analysis.py file
    final = Input.translate(str.maketrans(string.ascii_lowercase, Key))
    return final


def md5_cracker_with_sub_cipher(Input):  # use this to test if user1 has any SALT or leet speak
    with open('dictionary.txt') as dic:
        password = dic.readline().strip('\n')
        while password:
            finalpass = password
            finalpass2 = substitution_cipher_decoder(finalpass)
            PasswordInHex = hashlib.md5(finalpass2.encode('utf-8'))
            if PasswordInHex.hexdigest() == Input:
                print(password)
                exit()
            password = dic.readline().strip('\n')
        dic.close()
        # this give user7 password: leprechaun with md5 and sub cipher


def main():
    Input = input("Input the string u want to crack: ")
    if len(Input) == 32:
        md5_cracker_test(Input)
        md5_cracker_with_sub_cipher(Input)
    elif len(Input) == 40:
        sha1_cracker_test(Input)
        sha1_cracker_leet_speak_test(Input)
    elif len(Input) == 64:
        sha256_cracker(Input)
        sha256_with_SALT(Input)
    elif len(Input) == 128:
        sha512_cracker(Input)
        sha512_with_caesar_cipher(Input)


if __name__ == "__main__":
    main()
