#!/usr/bin/env python

import socket


TCP_IP = input("Insira o IP do servidor: ")
TCP_PORT = input("Insira a porta: ")
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)
