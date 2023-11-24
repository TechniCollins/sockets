import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())

# Define the socket
# First argument is the family/category of sockets
# Second argument is transmission mode? In this case streaming? Do more research on this.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to our server IP address on port 6009
# the bind method takes a tuple in this format (ADDRESS, PORT)
server_socket.bind((SERVER_IP, 6009))


# The function below will run in a new thread
# It will handle incoming socket communications from clients
def client_handler(client_socket, client_address):
    print(f"New connection: {client_address}")
    
    while True:
        message_length = client_socket.recv(128).decode("utf-8")
        message_length = int(message_length)
        message = client_socket.recv(message_length).decode("utf-8")
        # The block above waits to receive a 128 byte message from the client
        # The message is then decoded from bytes to utf8 format

        if message: # Check that the client is not sending an empty message
            print(f"{client_address} : {message}") # Print the message sent by the client

            # Cleanly disconnect the client if the message is #?DisconnectSignal?#
            if message == "#?DisconnectSignal?#":
                client_socket.send("Server received disconnection command".encode("utf-8"))
                break # Stop the loop

            # Send a utf8-encoded acknowledgment message back to the client
            client_socket.send("Server received message".encode("utf-8"))

    client_socket.close()


server_socket.listen()

# Run an infinite loop
while True:
    # Wait for a new connection, then capture the client
    # socket object and client address (IP address + Port)
    # into variables
    client_socket, client_address = server_socket.accept()

    # Run the handler function on a new thread (t)
    # Pass the variables above to the handler
    t = threading.Thread(target=client_handler, args=(client_socket, client_address))
    t.start() # Start the thread

    # Output the total number of connections
    print(f"The server is handling {threading.active_count() - 1} connections")

