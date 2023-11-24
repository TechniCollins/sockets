import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, 6007)) # Connect to the address defined in the server script

# We first send the message length, then the actual message -> Why?
# I'm not sure, but if I don't do this, the server concatnates different messages -> Do some research 


def send(message):
	message = message.encode("utf-8") # The message to be sent to the server (utf8 encoded)
	message_length = len(message)

	# Fill message length with spaces -> Why is this necessary? Again, I don't know. Consult.
	padded_message = str(message_length).encode('utf-8')
	padded_message += b' ' * (128 - len(padded_message))

	client_socket.send(padded_message) # Send the length of the message, space-padded to fit 128 bytes
	client_socket.send(message) # Send a utf-8 encoded message to the server

	# Print the response from the server
	print(client_socket.recv(128))
	print("Press any button to continue")
	input() # Just to pause the client for testing purposes

send("Sockets are awesome... I think :)")
send("Roses are black, violets are green")
send("Big time rush")
send("#?DisconnectSignal?#") # Send the predefined disconnect message
