import socket
import threading
from _thread import *
from queue import *
import time 
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 3000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    # List of sockets for select.select()
    sockets_list = [server_socket]
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data1 = "You are connected with server"
        conn.send(data1.encode())  # send data to the client
        data2="Enter a message"
        conn.send(data2.encode())
        m=float(input("Enter maximum life time of message"))
        s=float(input("Enter the max. scew time of a message"))
        m1=float(round(time.time()*1000))
        data3 = conn.recv(1024).decode()
        print("received data is %s \n"%data3)
        G = m1-m-s
        print("G = ",G)
        cu_time=float(time.time())
        
        if cu_time < G:
            print("Message accepted")
            k="Message accepted"
            conn.send(k.encode())
            print("Message accepted")
        else:
            d="Message is rejected"
            conn.send(d.encode())
            print("Message rejected")
        
if __name__ == '__main__':
    server_program()
        
        
        
