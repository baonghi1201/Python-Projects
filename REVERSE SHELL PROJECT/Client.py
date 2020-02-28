import socket
import os
import subprocess

s=socket.socket()
host='192.168.1.12'
port= 1201

s.connect((host,port))


