import socket
import os
import subprocess
import time


WAIT_TIME = 5


udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 4040)) 

print("UDP server listening for file...")  


data, client_address = udp_server.recvfrom(4096)   
filename = data.decode()   

with open(filename, 'wb') as f:
    while True:
        data, client_address = udp_server.recvfrom(4096)
        if data == b'EOF':  
            break
        f.write(data)

print(f"File '{filename}' received successfully.")
udp_server.close()

print(f"Opening '{filename}' in {WAIT_TIME} seconds...")
time.sleep(WAIT_TIME)

try:
    if os.name == 'nt': 
        os.startfile(filename)
    elif os.name == 'posix':  
        subprocess.run(['open', filename]) 
except Exception as e:
    print(f"Error while trying to open the file: {e}")