import socket


udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4040)

def send_file(filename):
    
    udp_client.sendto(filename.encode(), server_address)

    with open(filename, 'rb') as f:
        chunk = f.read(4096)  
        while chunk:
            udp_client.sendto(chunk, server_address)
            chunk = f.read(4096)  

    udp_client.sendto(b'EOF', server_address)

    print(f"File '{filename}' sent successfully.")

send_file('samplevideo.mp4')
udp_client.close()
