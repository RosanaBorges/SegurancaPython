#relacionamento entre rede e sistema operacional

import socket
# fornece acesso a variáveis e funções que tem forte interação com python
import sys

#definição de função para conexão IP e TCP
def main():
    try:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print ('Falha na conexão')
        print ('Erro: {}'.format(erro))
        sys.exit()

    print ('Socket criado com sucesso')

    #conexão com host

    hostalvo = input('Digite o host ou ip a ser conectado:  ')
    portaalvo = input('Digite a porta a ser conectada:  ')

    #conexão
    try:
        s.connect((hostalvo, int(portaalvo))) #tranformação string para int para o s.connect aceitar
        print('Cliente TCP conectado com sucesso nos host:'+ hostalvo+'e na porta'+ portaalvo)
        s.shutdown(2) # fechar a conexão para não ficar no loop

    except socket.error as erro:
        print('Conexão falhou')
        print ('Erro:'.format(erro))
        sys.exit()

#chamar função main
if __name__== '__main__':
    main()