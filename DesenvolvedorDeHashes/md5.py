#Biblioteca que implementa uma interface comum para muitos algoritmos de hash seguro por exemplo SHA1, SHA256, MD5 entre outros
import hashlib

string = input('Digite texto para gerar hash:')

#codificação de caracteres utf-8
resultado = hashlib.md5(string.encode ('utf-8'))

#hexdigest retornado como uma string de comprimento duplo, contendo apenas dígitos hexadecimais.
# Isso pode ser usado para trocar o valor com segurança em e-mail ou outros ambientes não binários.
print('O hash da string é: ', resultado.hexdigest())