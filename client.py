import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, 6007)) # Connect to the address defined in the server script

