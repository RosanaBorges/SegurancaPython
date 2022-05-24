#servidor criado para interagir com cliente
#relacionamento entre rede e sistema operacional
import socket
# fornece acesso a variáveis e funções que tem forte interação com python
import sys

#objeto de conexão
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM,)

print('Cliente Socket criado com sucesso!')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem ='\nServidor: Olá Cliente!Tudo beM?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)