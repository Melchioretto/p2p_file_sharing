from concurrent.futures import thread
import socket
import threading

IP_SERVIDOR = socket.gethostbyname(socket.gethostname())
PORT = 2000
ADDR = (IP_SERVIDOR, PORT)
PORT_PEER = 2001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []

def novo_peer():
    print ("[NOVA CONEXÃO] {addr}")
    global conexoes
    
    
def inicio():
    print("[INICIANDO] socket.")
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=novo_peer, args=(conn, addr))
        thread.inicio()
        
inicio()