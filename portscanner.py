#!/usr/bin/python3

import socket
import sys

args = sys.argv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if len(args) < 2:
  host = input("Please enter the IP address you want to scan: \r\n")
  port = int(input("Please enter the port you want to scan: \r\n"))
else:
  host = args[1]
  port = int(args[2])

def portScanner(port):
    # set the timeout to 5 seconds so that the scan doesn't take forever
    s.settimeout(5)
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)