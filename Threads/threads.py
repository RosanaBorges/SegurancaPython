#Multithreads (paralelismo) fazer um programa que envia e recebe pacotes ao mesmo tempo através de threads
from threading import Thread
import time

def carro (velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n'.format(piloto, trajeto))

t_carro1 = Thread(target=carro, args=[5, 'Gohan'])
t_carro2 = Thread(target=carro, args=[4, 'Goten'])

t_carro1.start()
t_carro2.start()