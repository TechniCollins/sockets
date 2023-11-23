import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())

# Define the socket
# First argument is the family/category of sockets
# Second argument is transmission mode? In this case streaming? Do more research on this.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to our server IP address on port 6007
# the bind method takes a tuple in this format (ADDRESS, PORT)
server_socket.bind((SERVER_IP, 6007))
