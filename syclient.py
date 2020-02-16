import socket
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 3000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    message = input(" -> ") 
    if message.lower().strip() != 'bye':
        message = input(" -> ") 
        client_socket.send(message.encode())
        client_socket.recv(1024).decode()
        client_socket.recv(1024).decode()
        message1 = input(" Enter data   \t-> ")
        client_socket.send(message1.encode())
        client_socket.recv(1024).decode()
        client_socket.recv(1024).decode()
        client_socket.recv(1024).decode()
        client_socket.close()
        if(message== None):
            client_socket.close()
if __name__ == '__main__':
    client_program()


