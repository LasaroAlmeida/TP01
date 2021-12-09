## Lásaro de Almeida Deodoro --------- 09/12/21
import socket
def main():
    name_server = input("Host: ")
    port_server = int(input("Port: "))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    try:
        client_socket.connect((name_server, port_server)) # Tenta se conectar ao servidor
    except socket.error:
        print(f"Could not connect to {(name_server, port_server)}") 
    else:
        while True: #Enquato estiver conectado ao servidor
            message = input("M:> ") #Entra com a mensagem
            if(message != ""):
                client_socket.send(message.encode()) #envia para o servidor a mensagem em codificada
                print("[*MESSAGE SENT*]")
                if message[:4] == "quit": 
                    print("CLOSED CONNECTION")
                    break 
                else:
                    response = client_socket.recv(2048) #Recebe resposta do servidor
                    print(f"[RESPONSE:] {response.decode()}")
    client_socket.close() #Fecha o socket criado

if __name__ == "__main__":
    main()
