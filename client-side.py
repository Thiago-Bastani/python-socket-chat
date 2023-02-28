import socket
from sys import stdout
import threading

# Define o endereço e a porta do servidor
HOST = 'localhost'  # endereço do servidor
PORT = 8088        # porta do servidor

# Cria um objeto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((HOST, PORT))
nome = input("Nome: ")

def receive():
    """
    Recebe mensagens do servidor e as imprime na tela.
    """
    while True:
        try:
            mensagem = client_socket.recv(1024).decode()
            stdout.write(f'\r{mensagem}\n{nome}: ')
        except:
            # Encerra a conexão se não for possível receber a mensagem
            client_socket.close()
            break

def send():
    """
    Lê mensagens digitadas pelo usuário e as envia ao servidor.
    """
    while True:
        mensagem = input(f"{nome}: ")
        mensagem = f'{nome}: {mensagem}'
        client_socket.send(mensagem.encode())

# Inicia as threads para receber e enviar mensagens
threading.Thread(target=receive).start()
threading.Thread(target=send).start()
