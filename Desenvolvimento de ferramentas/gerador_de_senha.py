#biblioteca para gerarsenhas aleatórias, ramdomizar letras e números
import random
import string

#tamanho_senha = 16

estrutura_senha = string.ascii_letters + string.digits+ '/*-+._!@#$%¨&*(){}[]?`´<>Ç,^~|' #envolve letras maiuscula e minuscula

#caso usuário queira colocar um limite no tamanho da senha
tamanho_senha = int (input('Digite o número do tamanho da senha: '))

rnd = random.SystemRandom()
# ira alternar em estrutura de senha  de acordo com tamanho senha
print(''.join(rnd.choice(estrutura_senha)for i in range (tamanho_senha)))