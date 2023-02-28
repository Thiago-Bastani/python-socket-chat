import socket
import threading

# Define o endereço e a porta do servidor
HOST = 'localhost'  # endereço do servidor
PORT = 8088       # porta do servidor

# Cria um objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind do socket ao endereço e porta do servidor
server_socket.bind((HOST, PORT))

# Coloca o socket em modo de escuta
server_socket.listen()

# Lista de clientes conectados
clientes = []

def broadcast(mensagem, remetente):
    """
    Envia uma mensagem para todos os clientes conectados, exceto o remetente.
    """
    for cliente in clientes:
        if cliente != remetente:
            try:
                cliente.send(mensagem.encode())
            except:
                # Remove o cliente da lista se não for possível enviar a mensagem
                clientes.remove(cliente)

def handle_cliente(cliente):
    """
    Lida com as mensagens recebidas do cliente.
    """
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            broadcast(mensagem, cliente)
        except:
            # Remove o cliente da lista se não for possível receber a mensagem
            clientes.remove(cliente)
            break

# Aguarda por conexões de clientes
print(f"Aguardando por conexões na porta {PORT}...")
while True:
    cliente, endereco = server_socket.accept()
    clientes.append(cliente)
    print(f"Conexão estabelecida com o cliente {endereco}")
    threading.Thread(target=handle_cliente, args=(cliente,)).start()