#Biblioteca que implementa uma interface comum para muitos algoritmos de hash seguro por exemplo SHA1, SHA256, MD5 entre outros
import hashlib

string = input('Digite texto para gerar hash:')

menu = int(input('''##########MENU##########
                1)MD5
                2)SHA1
                3)SHA256
                4)SHA512
                Digite o número da HASH a ser gerado:'''))

if menu ==1:
    resultado = hashlib.md5(string.encode ('utf-8'))
    print(' A HASH MD5 da string : ', string, 'é:', resultado.hexdigest() )

elif menu ==2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(' A HASH SHA1 da string : ', string, 'é:', resultado.hexdigest())

elif menu ==3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(' A HASH SHA256 da string : ', string, 'é:', resultado.hexdigest())

elif menu ==4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(' A HASH SHA512 da string : ', string, 'é:', resultado.hexdigest())

else:
    print('Opção invalida, por favor tente novamente.')


