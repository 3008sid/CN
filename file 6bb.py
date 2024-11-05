
############################CLIENT.PY########################

import socket

host = "127.0.0.1"
port = 12000
buffer_size = 1024
file_name = 'Myfile22.txt'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

with open(file_name, "r") as f:  

    data = f.read(buffer_size)
    while data:
        print(data) 
        sock.sendto(data.encode(), (host, port)) 
        data = f.read(buffer_size)  

    sock.sendto("Now".encode(), (host, port))

sock.close()  # Close the socket