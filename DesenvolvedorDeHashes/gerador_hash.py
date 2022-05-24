#Biblioteca que implementa uma interface comum para muitos algoritmos de hash seguro por exemplo SHA1, SHA256, MD5 entre outros
import hashlib

#  b converte a string em bytes
resultado = hashlib.md5(b'Estou adorando o curso de Python Security')

#hexdigest retornado como uma string de comprimento duplo, contendo apenas dígitos hexadecimais.
# Isso pode ser usado para trocar o valor com segurança em e-mail ou outros ambientes não binários.
print('O hash da string é: ', resultado.hexdigest())