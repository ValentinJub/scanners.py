#!/usr/bin/python3

import socket

s = socket.socket()
ip = input("Enter the IP address of the target: ")
port = int(input("Enter the port number: "))

s.connect((ip, port))
print(s.recv(1024).decode("ascii"))