from http import client
import socket
import threading
from Servidor import IP_SERVIDOR, PORT, PORT_PEER, conexoes

peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

peer.connect(IP_SERVIDOR,PORT)

client.connect


def peers():
        print('\n'.join(map(str, conexoes)))
#seria melhor iniciar fazendo a busca de todos os
#peers conectados no servidor
def ls():
    pass


def get():
    pass


def sair():
    pass