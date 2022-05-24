#relacionamento entre rede e sistema operacional
import socket


s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM,)

print('Cliente Socket criado com sucesso!')

host = 'localhost'
porta = 5433
mensagem = 'Ola servidor'

#envio e recebimento de mensagem
try:
    #empacotamento da mensagem e envio para host, onde a porta 5432 estará "ouvindo"
    print('Cliente: '+ mensagem)
    s.sendto(mensagem.endcode(), (host,5432))
#  receber a responsta do servidor onde os dados irão desempacotar os dados e imprimir a resposta
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print ('Cliente: '+ dados)
#fechamento de conexão para não ficar em loop
finally:
    print('Cliente: Fechando a conexão')
    s.close()