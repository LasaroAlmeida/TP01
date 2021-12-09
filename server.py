## Lásaro de Almeida Deodoro --------- 09/12/21
import socket
import threading

def input_manipulation(text_in):  # divide o texto em duas partes
    i = text_in.find(' ')
    return [text_in, " "] if (i == -1) else [text_in[0:i], text_in[(i+1):]]

def client_connection(connection_socket): # Função que vai tratar a conexão com cada um dos clientes
    connected = True
    while connected:
        message = connection_socket.recv(2048).decode() # Recebe e decodifica a mensagem do cliente
        message_parts = input_manipulation(message)
        print(f"[{message}]")
        if message_parts[0] == "quit":  # Termina a conexão quando for o comando quit
            print("CLOSED CONNECTION")
            connected = False
        elif message_parts[0] == "echo": # Envia o corpo da mensagem ao cliente caso o comando seja echo
            connection_socket.send(message_parts[1].encode())
        else:  # Informa erro quando o comando for inválido
            connection_socket.send("[*ERROR*]".encode())
    connection_socket.close()  # Fecha o socket


def main():
    # definem o host e a porta para o servidor
    host = '' # localhost
    port = 4444
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
    server_socket.bind((host, port))  # Atribui host e port ao socket
    server_socket.listen()  # Socket esta esperado por um cliente
    print(f"Server listening localhost on port {port}")
    while True:
        connection_socket, address = server_socket.accept() # Recebe o cliente e o designa um novo socket
        print(f"connection accepted {address}")
        thread = threading.Thread(
            target=client_connection, args=(connection_socket,))  # Cria uma thread para atender o cliente
        thread.start()  # Inicia a thread; Executa a função client_connection


if __name__ == "__main__":
    main()
