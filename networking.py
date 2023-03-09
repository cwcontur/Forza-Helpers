import os
from socket import *

host = "192.168.86.36" # IPV4
port = 10000
buf = 1024

address = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(address)
def receive():



    print ("Waiting to receive messages...")

    while True:
        (data, address) = UDPSock.recvfrom(buf)
        print("Received message: " + data.decode())





# if data == b"exit":
#     break


    UDPSock.close()
    os._exit(0)