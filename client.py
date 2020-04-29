import socket
import os
import subprocess

s = socket.socket()
host = '104.236.209.167'
port = 9999

s.connect((host, port))

filename = "test.txt"
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully")
