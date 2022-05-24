import hashlib

arq1 = 'arquivo1.txt'
arq2 = 'arquivo2.txt'

#definição de qual construtor vai utilizar escolhido é um algoritmo de hash de 160 bits
hash1 = hashlib.new('ripemd160')

#Comparação do Hash qual frase será comparada
hash1.update(open(arq1, 'rb').read())

#definição de qual construtor vai utilizar escolhido é um algoritmo de hash de 160 bits
hash2 = hashlib.new('ripemd160')

#Comparação do Hash qual frase será comparada
hash2.update(open(arq2, 'rb').read())

#comparação digest siginifica resumido

if hash1.digest() !=  hash2.digest():
    print (f'O item: {arq1} é diferente do item: {arq2}')
    # aparece o número hexadecimal do hash
    print ('O hash do arquivo1.txt é: ', hash1.hexdigest())
    print ('O hash do arquivo2.txt é: ', hash2.hexdigest())
else:
    print(f'O item: {arq1} é igual do item: {arq2}')
    # aparece o número hexadecimal do hash
    print ('O hash do arquivo1.txt é: ', hash1.hexdigest())
    print ('O hash do arquivo2.txt é: ', hash2.hexdigest())
